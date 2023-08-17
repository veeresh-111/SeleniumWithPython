from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

serv_obj = Service("C:\WebDrivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# driver.save_screenshot("C:\\Users\\hp\\PycharmProjects\\MyfirstProject\\Day13\\homepage.png")
# driver.save_screenshot(os.getcwd()+"\\homepage.png")
driver.get_screenshot_as_file(os.getcwd()+"\\homepage.png")
# driver.get_screenshot_as_png() # save screenshot in encode formate
# driver.get_screenshot_as_base64()  # save screenshot in encode formate
driver.quit()