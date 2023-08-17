import time

from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By


serv_obj=Service("C:\WebDrivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
time.sleep(3)

# self
text_msg=driver.find_element(By.XPATH,"//*[@id='leftcontainer']/table/tbody/tr[1]/td[1]/a").text
print(text_msg)   # Jindal St & Pwr

# Parent
# text_msg=driver.find_element(By.XPATH,"//a[contains(.,'Jindal St & Pwr')]/parent::td").text
# print(text_msg)  # Jindal St & Pwr

# Child
# childs=driver.find_elements(By.XPATH,"//a[contains(.,'Jindal St & Pwr')]/ancestor::tr/child::td")
# print("Number of child Nodes:",len(childs))  # 5

# Ancestor
# text_msg=driver.find_element(By.XPATH,"//a[contains(.,'Jindal St & Pwr')]/ancestor::tr").text
# print(text_msg)  # Jindal St & Pwr A 544.90 575.00 + 5.52

# Descendent
# descendants=driver.find_elements(By.XPATH,"//a[contains(.,'Jindal St & Pwr')]/ancestor::tr/descendant::*")
# print("Number of descendants Nodes:",len(descendants))  # 7

# Following
# followings=driver.find_elements(By.XPATH,"//a[contains(.,'Jindal St & Pwr')]/ancestor::tr/following::*")
# print("Number of Following Nodes:",len(followings))  # 3203

# Following-sibling
# followingsiblings=driver.find_elements(By.XPATH,"//a[contains(.,'Jindal St & Pwr')]/ancestor::tr/following-sibling::*")
# print("Number of Following-sibling Nodes:",len(followingsiblings))  # 391

# Preceding
# precedings=driver.find_elements(By.XPATH,"//a[contains(.,'Jindal St & Pwr')]/ancestor::tr/preceding::*")
# print("Number of Preceding Nodes:",len(precedings))  # 221

# Preceding-sibling
# precedingsiblings=driver.find_elements(By.XPATH,"//a[contains(.,'Jindal St & Pwr')]/ancestor::tr/preceding-sibling::*")
# print("Number of Preceding-sibling Nodes:",len(precedingsiblings))  # 4
#
# driver.close()