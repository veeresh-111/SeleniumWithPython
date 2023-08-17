import time

from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By


serv_obj=Service("C:\WebDrivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#Absolute xpath

# driver.find_element(By.XPATH,"/html/body/div[6]/div[1]/div[2]/div[2]/form/input").send_keys("Apparel")
# driver.find_element(By.XPATH,"/html/body/div[6]/div[1]/div[2]/div[2]/form/button").click()

#Relative xpath
# driver.find_element(By.XPATH,"//*[@id='small-searchterms']").send_keys("Apparel")
# driver.find_element(By.XPATH,"//*[@id='small-search-box-form']/button").click()

# or, and operator
# driver.find_element(By.XPATH,"//input[@id='small-searchterms' or @name='q']").send_keys("Apparel")
# driver.find_element(By.XPATH,"//button[@class='button-1 search-box-button' and @type='submit']").click()

# contains() and Starts-with()
# driver.find_element(By.XPATH,"//input[contains(@id,'small')]").send_keys("Apparel")
# driver.find_element(By.XPATH,"//button[starts-with(@class,'button-1 search')]").click()

#Text()
driver.find_element(By.XPATH,"//a[text()='Register']").click()