import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



#passe la commande/////
browser = webdriver.Chrome('C:/Users/neelg/Documents/dep/chromedriver.exe')
browser.get("https://www.nike.com/fr/t/chaussure-air-vapormax-2020-fk-pour-kWs8Sn/CJ6740-002")


button = browser.find_element_by_xpath('//*[@id="buyTools"]/div[1]/fieldset/div/div[11]/label')#taille(45)
button.click()

button = browser.find_element_by_xpath('//*[@id="floating-atc-wrapper"]/div/button[1]')#(bouton commander)
button.click()

time.sleep(0.5)

button = browser.find_element_by_xpath('//*[@id="PDP"]/div/div[4]/div/div/div/div/div/div/div/div/div/div[3]/div/button[2]')
button.click()

time.sleep(5)

#checkout/////
#name
button = browser.find_element_by_xpath('//*[@id="firstName"]')
button.click()
element = button
element.send_keys("Neel")

#lastname
button = browser.find_element_by_xpath('//*[@id="lastName"]')
button.click()
element = button
element.send_keys("Grévy")

#adress
button = browser.find_element_by_xpath('//*[@id="search-address-input"]')
button.click()
element = button
element.send_keys("46 Rue raymond ridel")

#Gmail
button = browser.find_element_by_xpath('//*[@id="email"]')
button.click()
element = button
element.send_keys("neel.grevy@gmail.com")

#tel
button = browser.find_element_by_xpath('//*[@id="phoneNumber"]')
button.click()
element = button
element.send_keys("0600000000")

