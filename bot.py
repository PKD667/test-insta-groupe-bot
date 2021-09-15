
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
exeption = []
indice =  True
retro = ""
def setup(exeption) :
   texte_init = browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div').text
   test_liste_init =  texte_init.split()
   for m in range(len(test_liste_init)) :
      exeption.append(test_liste_init[m])
   return exeption
def analyse (exeption) :  
   texte = browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div').text
   test_liste =  texte.split()
   mot = test_liste[-1]
   exeption = test_liste
   print(test_liste)
   if indice == True :
     if mot == 'Salut' or 'salut' or 'wsh' or 'Wsh' or 'Bonjour' or 'bonjour' :
         area.send_keys('Wsh mon gars ca va toi ?')
         sleep(0.5)
         browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
     if mot[0:1] == "!" :
          if mot[1:] == "kill" :
             area.send_keys('Booom,boom,boom')
             sleep(0.5)
             browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()     
   return exeption
setup(exeption)
while 1 :
  exeption = analyse(indice)
  indice = True
  if exeption == retro :
    indice = False
  retro = exeption