import time

from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By


serv_obj=Service("C:\WebDrivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.get("https://admin-demo.nopcommerce.com/login")
time.sleep(3)
emailbox=driver.find_element(By.XPATH,"//input[@id='Email']")
emailbox.clear()
emailbox.send_keys("abc@gmail.com")
print("Result of text:",emailbox.text)
print("Result of get_attribute:",emailbox.get_attribute('value'))
print("Result of get_attribute:",emailbox.get_attribute('type'))

# button=driver.find_element(By.XPATH,"//button[normalize-space()='Log in']")
# print("Result of text:",button.text)
# print("Result of get_attribute:",button.get_attribute('value'))
# print("Result of get_attribute:",button.get_attribute('type'))