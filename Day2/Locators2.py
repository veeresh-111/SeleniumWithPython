import time

from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\WebDrivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
time.sleep(3)
driver.get("https://automationexercise.com/")
driver.maximize_window() # maximize window

# Class Name and TagName locators:
sliders=driver.find_elements(By.CLASS_NAME,"active")
print(len(sliders)) #3 total slides

links=driver.find_elements(By.TAG_NAME,'a')
print(len(links)) # total number of links on home page  #147

# driver.close()
# driver.quit()