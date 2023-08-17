import time

from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\WebDrivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# click on link
#driver.find_element(By.LINK_TEXT,"Digital downloads").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"Digital").click()

# find total number of links in a page
#links=driver.find_elements(By.TAG_NAME,'A')
links=driver.find_elements(By.XPATH,"//a")
print("total number of links:",len(links)) # 90

# print all links name
for link in links:
    print(link.text)