import time

from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By


serv_obj=Service("C:\WebDrivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get("https://demo.nopcommerce.com/")

######### find_element() - Returns sinlge web element

#1) Locate matching single webelement
# element=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
# element.send_keys("Apple MacBook Pro 13-inch")

#2) Locate matching multiple webelement
# element=driver.find_element(By.XPATH,"//div[@class='footer']//a") # it returns first matching element
# print(element.text) # Sitemap

#3) elements not available nosuchelements exception
# login_element=element=driver.find_element(By.LINK_TEXT,"Log")
# login_element.click()  #selenium.common.exceptions.NoSuchElementException: Message: no such element:
# # Unable to locate element: {"method":"link text","selector":"Log"}


######### find_elements() - Returns Multiple web element

#1) Locate matching single webelement
# elements=driver.find_elements(By.XPATH,"//input[@id='small-searchterms']")
# print(len(elements)) # 1
# elements[0].send_keys("Apple MacBook Pro 13-inch")

#2) Locate matching multiple webelement
# elements=driver.find_elements(By.XPATH,"//div[@class='footer']//a")
# print(len(elements)) # 23
# #print(elements[0].text) # Sitemap
# for ele in elements:
#     print(ele.text)

#3) elements not available
elements=element=driver.find_elements(By.LINK_TEXT,"Log")
print("Returned elements:",len(elements))  # return 0