import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv_obj=Service("C:\WebDrivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10) # seconds # implicit wait

driver.get("https://www.google.com/")
driver.maximize_window()

search_box=driver.find_element(By.NAME,"q")
search_box.send_keys("selenium")
search_box.submit()

driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()
driver.quit()