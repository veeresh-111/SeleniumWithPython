import time

from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By


serv_obj=Service("C:\WebDrivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get("https://demo.nopcommerce.com/register")
time.sleep(3)

# is_displayed() &  is_enabled()
search_box=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
print("Displayed status:",search_box.is_displayed()) # true
print("Enabled status:",search_box.is_enabled())     # true

# is_selected
rd_male=driver.find_element(By.XPATH,"//input[@id='gender-male']")
rd_Female=driver.find_element(By.XPATH,"//input[@id='gender-female']")

print("default radio button status.....")
print(rd_male.is_selected())  #false
print(rd_Female.is_selected()) #false

rd_male.click()  # select male radio button
print("After selecting male raio button.....")
print(rd_male.is_selected())  #true
print(rd_Female.is_selected()) #false

rd_Female.click()  # select fe-male radio button
print("After selecting fe-male raio button.....")
print(rd_male.is_selected())  #false
print(rd_Female.is_selected()) #true

driver.close()