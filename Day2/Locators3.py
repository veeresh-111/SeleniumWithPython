import time

from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\WebDrivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
time.sleep(3)
driver.get("https://www.facebook.com/")
driver.maximize_window() # maximize window

# tag and id CSS selector combo
# driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc")
# driver.find_element(By.CSS_SELECTOR,"#email").send_keys("abc")

# tag and class CSS selector combo
driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("abc")
driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("abc")

# Tag and attribute combo
# driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys("abc@gmail.com")
# driver.find_element(By.CSS_SELECTOR,"[data-testid=royal_email]").send_keys("abc@gmail.com")

# Tag, class and attribute combo
# driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_pass]").send_keys("xyz")
# driver.find_element(By.CSS_SELECTOR,".inputtext[data-testid=royal_pass]").send_keys("xyz")

# driver.close()
# driver.quit()