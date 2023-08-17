import time
from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\WebDrivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)


driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.switch_to.frame(0)  # switch to frame

# driver.find_element(By.XPATH,"//*[@id='datepicker']").send_keys("05/30/2023") # mm/dd/yyyy

year="2022"
month="June"
date="1"

driver.find_element(By.XPATH,"//*[@id='datepicker']").click() #opens datepicker

while True:
    mon=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yr=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text

    if mon==month and yr==year:
        break
    else:
        #driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click() # next arrow
        driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-w']").click() # previous arrow

# select date
dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for ele in dates:
    if ele.text==date:
        ele.click()
        break


print("Done..............")
driver.close()