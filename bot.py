
#instagram password : ezf449ezfezfzf 
#instagram username : clude.kirsky
#mail adress : groupe.insta.test@gmail.com  =========legacy
#mail password : 89zf8fz98f7z98f7z98f7z97   ===========legacy

#//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div[4]

import json  
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import string,random,threading
from time import sleep
# Initiate the browser
browser  = webdriver.Chrome(ChromeDriverManager().install())
def login() :
  grp_list = []
  browser.get('https://www.instagram.com/direct/inbox')
  browser.find_element_by_class_name('aOOlW.bIiDR').click()
  sleep(1)
  browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys('claude.kirsky')
  browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys('ezf449ezfezfzf')
  browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
  sleep(5)
  browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
  sleep(2)
  browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
  sleep(2)
  g = 1
  try :
    while True :
       grp_name = browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[' + str(g) + ']/a/div/div[2]/div[1]/div/div/div/div')
       grp_list.append(grp_name.text)
       g +=1 
  except Exception :
     pass
  number = input(str(grp_list) + " : ")
  browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div['+ number +']/a').click()
  sleep(2)

def initialize(file_path) :
 with open(file_path, 'r') as output_file:
   readed = output_file.read()
   response_dict = readed
   print(response_dict)
   response_dict = json.loads(response_dict) 
   return response_dict

def texted(texte) :
   browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(texte)
   sleep(0.5)
   browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click() 
   return texte

def ordering(order,back,response_dict) :
   texte = ""
   global Break
   try : 
      go = response_dict[order]
      texte = texted(go)
      print('correlation found')
   except Exception:
      pass
   if order[0:1] == "!" :
      special = order[1:]
      format_special = special.split(":")
      if format_special[0] == "kill" :
         texte = texted("boom!,boom!,boom!")
         Break = True
      if format_special[0] == "add" :
         with open(file_path, 'w') as output_file:            
            response_dict[format_special[1]] = format_special[2].replace("_"," ")
            output_file.write(json.dumps(response_dict))
            print(response_dict)
      if format_special[0] == "remove" :
         del response_dict[format_special[1]]
   else : 
      pass
      if texte != "" :
        back = back.append(texte)
   return back,response_dict


def analyse (back,del_list) :  
   texte = browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div').text
   test_liste =  texte.split()
   for i in range(len(del_list)) :
     try :
      test_liste.remove(del_list[i])
     except Exception :
        pass
   if back != test_liste :
     mot = test_liste[-1]
   else :
      mot = 'none'
   try :
     with open(r"C:\Users\paulk\Desktop\web bot\insta-groupe-test\log.log","a") as log:
      log.write(mot)
   except :
      pass
   return mot,test_liste


del_list = ["En","train","d’écrire..."]
back = ""
file_path = r"C:\Users\paulk\Desktop\web bot\insta-groupe-test\dict_save.bot"
Break = False
login()
response_dict = initialize(file_path)


for i in range(10000000) :
  if Break == True :
     break
  texte = ""
  sortie_analyse = analyse(back,del_list)
  mot = sortie_analyse[0]
  back = sortie_analyse[1]
  sortie_order = ordering(mot,back,response_dict)
  back = sortie_order[0]
  response_dict = sortie_order[1]