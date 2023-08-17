from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\WebDrivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

minslider=driver.find_element(By.XPATH,"//span[1]")
maxslider=driver.find_element(By.XPATH,"//span[2]")

print("locaton of slioders before moving...")
print(minslider.location) # {'x': 59, 'y': 250}
print(maxslider.location) # {'x': 545, 'y': 250}

act=ActionChains(driver)
act.drag_and_drop_by_offset(minslider,100,0).perform()
act.drag_and_drop_by_offset(maxslider,-45,0).perform()

print("locaton of sliders after moving...")
print(minslider.location) # {'x': 161, 'y': 250}
print(maxslider.location) # {'x': 501, 'y': 250}