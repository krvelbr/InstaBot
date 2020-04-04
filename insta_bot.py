from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#from selenium.webdriver.common.by import By

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=r'c:\x\geckodriver.exe')
        
    
# //input[@name=username]
# //input[@name=password]

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com')
        time.sleep(3)  #espera 3 segundos pra carregar a pagina
        
        user_element = driver.find_element_by_xpath("//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)
        time.sleep(5)
        
    def curtir_fotos(self, hashtag):
        #self.hastag = hashtag
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/{}/'.format(hashtag))  #seleciona pela tag informada
        time.sleep(5)
        for i in range(1,4): #vai simular 4 descidas de paginas
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)    #vai dar um tempinho de 2 segundos pra poder carregar as imagens
        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]  #usado como lambda
        #para cada elem dentro de hrefs, ele ta buscando so os atributos href e armazenando na lista
        y = [x for x in pic_hrefs if 'https://www.instagram.com/p/' in x]  #pega so os links das fotos, pra nao pegar
                                                                        # os <a href> que nao sao fotos
        print(hashtag + ' fotos: ' + str(len(pic_hrefs))) #apenas pra debugar mesmo pra mim, pode tirar depois

        i=len(y)
        for pic_href in y:
            driver.get(pic_href)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            i -= 1
            print('Links para abrir: {}'.format(i))  #tambem pra me ajudar a debugar e ter ideia da qtde links
            
            try:
                time.sleep(1) #coloquei as pausas, so pra poder ver acontecendo, depois pode tirar quase todas
                driver.find_element_by_class_name('wpO6b').click()  ##  clica no botao curtir
                time.sleep(2)
                driver.find_element_by_class_name('wpO6b').click()  ## clica de novo pra desmarcar
                #aqui eu clico aguardo 2 segundos pra ver que clicou, e desmarco só pra ver funcionando
                
                time.sleep(6) # da um tempinho pro Insta nao achar que e um bot fazendo rapido demais
                #antes de ir pra proxima foto
            except Exception as e:
                print('Ocorreu o erro: {}'.format(e))
                time.sleep(4)
                #se deu algum erro, ele vai printar no terminal, pra poder ter uma idéia do que aconteceu






if __name__ == '__main__':
    
    hashtag = 'fortalezaordinaria'   #inserir aqui a hashtag de busca    
    instaBot = InstagramBot('username','password')   #informar usuario,senha
    instaBot.login()
    instaBot.curtir_fotos(hashtag)
