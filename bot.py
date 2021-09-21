
#instagram password : ezf449ezfezfzf =========legacy
#instagram username : claude.kirsky    ======legacy
#mail adress : groupe.insta.test@gmail.com  =========legacy
#mail password : 89zf8fz98f7z98f7z98f7z97   ===========legacy

#//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div[4]

import json
from os import kill  
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import threading
from time import sleep
# Initiate the browser

Queue = [[],[]]
Trou = True
response_dict = {}
text_queue = []
def ordering(order,file_path,response_dict) :
        Break = False
        order = order.lower()
        global text_queue
        try :
            go = response_dict[order]
            print('correlation found')
            text_queue.append(go)
        except Exception :
           pass
        if order[0:1] == "!" :
         try :
           special = order[1:]
           format_special = special.split(":")
           if format_special[0] == "kill" :
              Break = True
           elif format_special[0] == "add" :
              with open(file_path, 'w') as output_file:            
                 response_dict[format_special[1]] = format_special[2]
                 output_file.write(json.dumps(response_dict))       
           elif format_special[0] == "remove" :
                del response_dict[format_special[1]]
         except Exception :
            pass
        else : 
           pass
        return Break,response_dict

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
         texte = browser.find_elements_by_class_name('hjZTB')
         msg =  texte[-1].text
         if msg != prev :
                Queue[self.number-1].append(msg)
         prev = msg  
         if text_queue :
            browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(text_queue[0])
            print(text_queue[0])
            sleep(0.5)
            browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click() 
            del text_queue[0]

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
         sleep(2)
         global text_queue 
         global Queue
         print(text_queue,Queue)
         if Queue[self.number-1] != [] :
            sortie = ordering(Queue[self.number-1][0],file_path,response_dict)
            del Queue[self.number-1][0]
            Break = sortie[0]
            response_dict = sortie[1]
            
      kill

accounts = [["claude.kirsky","ezf449ezfezfzf"],["groupe_bot","Soniak23"],["groupe_bot02","Soniak23"]]
indices = 2

for i in range(1, 2 + 1) :
          browser = webdriver.Chrome(ChromeDriverManager().install())        
          th_W = WebThread(i,browser,accounts[indices][0],accounts[indices][1])
          th_run = RunThread(browser,i)
          th_W.start()
          th_run.start()
          