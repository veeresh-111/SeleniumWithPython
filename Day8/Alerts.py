import time

from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By


serv_obj=Service("C:\WebDrivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

#open alert window
driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(3)

alertwindow=driver.switch_to.alert
print(alertwindow.text) # I am a JS prompt
alertwindow.send_keys("welcome")
# alertwindow.accept() # click ok
alertwindow.dismiss()  # click cancel