import time

from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By


serv_obj=Service("C:\WebDrivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

# windowid=driver.current_window_handle
# print(windowid)  # 1B1FA4C235D823F83F33B166E55093D5

time.sleep(3)
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()

windowids=driver.window_handles

# Approach 1
# print(windowids)
#
# parentwindowid=windowids[0]
# childwindowid=windowids[1]
#
# print(parentwindowid,childwindowid)
#
# driver.switch_to.window(childwindowid)
# print(driver.title)
#
# driver.switch_to.window(parentwindowid)
# print(driver.title)

#Approach 2
# for winid in windowids:
#     driver.switch_to.window(winid)
#     print(driver.title)

time.sleep(3)
# Approach 3: close specific browser window
for winid in windowids:
    driver.switch_to.window(winid)
    if driver.title=='OrangeHRM HR Software | Free & Open Source HR Software | HRMS | HRIS | OrangeHRM':
        driver.close()