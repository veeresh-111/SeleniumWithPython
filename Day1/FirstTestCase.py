# Test case
# ------------------
# 1) Open web browser (chrome/Firefox/edge)
# 2) Open URL https://opensource-demo.orangehrmlive.com/
# 3) Provide Email (Admin)
# 4) Provide password (admin123)
# 5) Click on login.
# 6) Capture title of the dashboard page. (Actual title)
# 7) Verify title of the page: “OrangeHRM” (Expected)
# 8) close browser.


# Selenium 3
# import time
# from selenium import webdriver
#
# driver = webdriver.Chrome(executable_path="C:\WebDrivers\chromedriver.exe")
# #driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://opensource-demo.orangehrmlive.com/")
# time.sleep(3)
# driver.find_element_by_name("username").send_keys("Admin")
# time.sleep(3)
# driver.find_element_by_name("password").send_keys("admin123")
# time.sleep(3)
# str="//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']"
# driver.find_element_by_xpath(str).click()
# time.sleep(3)
# act_title = driver.title
# exp_title = "OrangeHRM"
# if act_title == exp_title:
#     print("Login Test Passed")
# else:
#     print("Login Test Failed")
# driver.close()

# Selenium 4
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\WebDrivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
#driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(3)
driver.maximize_window()
time.sleep(3)
driver.find_element(By.NAME, "username").send_keys("Admin")
time.sleep(3)
driver.find_element(By.NAME, "password").send_keys("admin123")
time.sleep(3)
str = "//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']"
driver.find_element(By.XPATH, str).click()
time.sleep(3)
act_title = driver.title
exp_title = "OrangeHRM"

if act_title == exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")

driver.close()
