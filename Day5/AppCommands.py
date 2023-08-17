import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv_obj=Service("C:\WebDrivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
print(driver.title)  # OrangeHRM
print(driver.current_url)  # https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
print(driver.page_source)

driver.close()