
#instagram password : ezf449ezfezfzf =========legacy
#instagram username : claude.kirsky    ======legacy
#mail adress : groupe.insta.test@gmail.com  =========legacy
#mail password : 89zf8fz98f7z98f7z98f7z97   ===========legacy

import json
from os import kill  
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import threading
from selenium.webdriver.common.keys import Keys
from time import sleep
# Initiate the browser
karma = 0
groups = 3
Trou = True
response_dict = {}
image_queue = []
Queue = []
text_queue = [[],[]]
   
for _ in range(groups) :
   image_queue.append([])
   Queue.append([])   
   text_queue.append([])

def ordering(order,file_path,response_dict,number) :
        with open("D:/insta-groupe-test/ordering.py","r") as ordering :
            code = ordering.read()
            exec(code)
            return response_dict
        

class WebThread(threading.Thread) :
   def __init__(self,number,browser,user,password) :
    threading.Thread.__init__(self)
    self.browser = browser
    self.user = user
    self.password = password
    self.number = number
   def run (self) :
      browser = self.browser
      browser.get('https://www.instagram.com/direct/inbox')
      browser.find_element_by_class_name('aOOlW.bIiDR').click()
      sleep(1)
      browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(self.user)
      browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(self.password)
      browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
      sleep(5)
      browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
      sleep(2)
      browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
      sleep(2)
      browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div['+ str(self.number) +']/a').click()
      sleep(2)
      prev = ""
      while Trou : 
         global Queue
         global text_queue  
         global image_queue
         sleep(0.5)
         texte = browser.find_elements_by_class_name('hjZTB')
         msg =  texte[-1].text
         if msg != prev :
                Queue[self.number-1].append(msg)
         prev = msg  
         if text_queue[self.number-1] :
            browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(text_queue[self.number-1][0] + Keys.ENTER)
            print(text_queue[self.number-1][0])
            del text_queue[self.number-1][0]
         if image_queue[self.number-1] :
            browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/button').click()
            file = "D:/insta-groupe-test/img.jpg"
            browser.find_element_by_name("uploadfile").send_keys(file + Keys.ENTER)
            print(text_queue[self.number-1][0])
            del image_queue[self.number-1][0]

class RunThread(threading.Thread) :
   def __init__(self,browser,number) :
    threading.Thread.__init__(self)
    self.browser = browser
    self.number = number
   def run (self) :
      global response_dict   
      file_path = r"D:\insta-groupe-test\dict.bot"
      Break = False      
      with open(file_path, 'r') as output_file:
         readed = output_file.read()
         response_dict = readed
         print(response_dict)
         response_dict = json.loads(response_dict) 
      while not Break :
         sleep(0.5)
         global text_queue 
         global Queue
         if Queue[self.number-1] != [] :
            response_dict = ordering(Queue[self.number-1][0],file_path,response_dict,self.number)
            del Queue[self.number-1][0]
      kill

accounts = [["claude.kirsky","ezf449ezfezfzf"],["groupe_bot","Soniak23"],["groupe_bot02","Soniak23"]]
indices = 1

for i in range(1, groups + 1) :
          browser = webdriver.Chrome(ChromeDriverManager().install())        
          th_W = WebThread(i,browser,accounts[indices][0],accounts[indices][1])
          th_run = RunThread(browser,i)
          th_W.start()
          th_run.start()
          