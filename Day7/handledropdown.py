import time

from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj=Service("C:\WebDrivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

#driver.get("https://www.opencart.com/index.php?route=account/register")
driver.get("https://testautomationpractice.blogspot.com")
driver.maximize_window()

# drpcountry_ele=driver.find_element(By.XPATH,"//select[@id='country']")
# drpcountry=Select(drpcountry_ele)
time.sleep(3)

# select options from dropdown
# drpcountry.select_by_visible_text("India")
# drpcountry.select_by_value("uk")
# drpcountry.select_by_index(8)

# capture all options and print them from dropdown
# alloptions=drpcountry.options
# print("total number of options:",len(alloptions))
#
# for opt in alloptions:
#     print(opt.text)

# select options from dropdown without built-in method
# for opt in alloptions:
#     if opt.text=="Canada":
#        opt.click()
#        break

# if no select tag then go directly option
alloptions=driver.find_elements(By.XPATH,"//*[@id='country']/option")
print("total number of options:",len(alloptions))

