from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui

serv_obj = Service("C:\WebDrivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.foundit.in/")
driver.maximize_window()

driver.find_element(By.XPATH,"//div[@class='heroSection-buttonContainer_secondaryBtn__text']").click()
driver.find_element(By.XPATH,"//input[@id='file-upload']").send_keys("E:\Form11Revised.pdf")

