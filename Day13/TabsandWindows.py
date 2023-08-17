from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

serv_obj = Service("C:\WebDrivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
regilink=Keys.CONTROL+Keys.RETURN
driver.find_element(By.LINK_TEXT,"Register").send_keys(regilink)

# New tab selenium 4: Open a new tab and switch to a new tab
# driver.get("https://www.opencart.com")
# driver.switch_to.new_window('tab')
# driver.get("https://www.orangehrm.com")

# New tab selenium 4: Open a new browser window and switch to a new window
# driver.get("https://www.opencart.com")
# driver.switch_to.new_window('window')
# driver.get("https://www.orangehrm.com")