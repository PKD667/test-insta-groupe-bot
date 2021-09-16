
#instagram password : ezf449ezfezfzf 
#instagram username : clude.kirsky
#mail adress : groupe.insta.test@gmail.com  =========legacy
#mail password : 89zf8fz98f7z98f7z98f7z97   ===========legacy

#//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div[4]

from re import I
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import string,random,threading
from time import sleep
import imaplib
import email
# Initiate the browser
browser  = webdriver.Chrome(ChromeDriverManager().install())
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
browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a').click()
sleep(2)
area = browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
back = ""
def input(texte) :
   area.send_keys(texte)
   sleep(0.5)
   browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click() 
   return texte
def ordering(order,back) :
   texte = ""

   if order == 'pas' :
      texte = input("nique ta mere fils de chien")
   elif order =='bonjour' :
         texte = input("Wsh mon gars ca va toi ?")
   elif order == 'quoi' :
      texte = input("feur")
   elif order[0:1] == "!" :
          special = order[1:]
          format_special = special.split(":")
          if format_special[0] == "kill" :
             texte = input("boom!,boom!,boom!")
          if format_special[0] == "image" :
             browser.get("google.com/search?q=" + format_special[1])
             browser.find_element_by_xpath("""//*[@id="hdtb-msb"]/div[1]/div/div[2]/a""").click()

   else :
      pass
      if texte != "" :
        back = back.append(texte)
   return back          


def analyse (back) :  
   texte = browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div').text
   test_liste =  texte.split()
   try :
     with open(r"C:\Users\paulk\Desktop\web bot\insta-groupe-test","a") as log:
      log.write(test_liste)
   except :
      pass
   if back != test_liste :
     mot = test_liste[-1]
   else :
      mot = 'none'
   return mot,test_liste
for i in range(10000000) :
  texte = ""
  print(i)
  sortie = analyse(back)
  mot = sortie[0]
  back = sortie[1]
  back = ordering(mot,back)
  try :
     with open(r"C:\Users\paulk\Desktop\web bot\insta-groupe-test\log.log","a") as log :
        log.write(back)
  except Exception :
     pass