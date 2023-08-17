import time

from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By


serv_obj=Service("C:\WebDrivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get("https://www.snapdeal.com")
time.sleep(3)
driver.get("https://amazon.com")

driver.back()  # to back snap deal page
time.sleep(3)
driver.forward() # to to amazon page

driver.refresh()

driver.quit()