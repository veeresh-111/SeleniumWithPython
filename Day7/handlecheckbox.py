import time

from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\WebDrivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

#1) select specific checkbox
# driver.find_element(By.XPATH,"//input[@id='monday']").click()

#2) select all the checkboxes
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkboxes)) # 7

# Approach 1
# for i in range(len(checkboxes)):
#     checkboxes[i].click()

# Approach 2
for checkbox in checkboxes:
    checkbox.click()

#3) Select multiple checkboxes by chaice
# for checkbox in checkboxes:
#     weekname=checkbox.get_attribute('id')
#     if weekname=='monday' or weekname=='sunday':
#          checkbox.click()

# 4) select last 2 checke boxes
# range(5,7) 6, 7
# totalnumberofelements-2=starting index
# for i in range(len(checkboxes)-2,len(checkboxes)):
#     checkboxes[i].click()

# 5) select first 2 check boxes
# for i in range(len(checkboxes)):
#     if i<2:
#         checkboxes[i].click()

time.sleep(5)
# 6) clearing all check boxes
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()