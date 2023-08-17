# CRTL+A
# CRTL+C
# TAB
# CRTL+V

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

serv_obj = Service("C:\WebDrivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://text-compare.com/")
driver.maximize_window()

input1 = driver.find_element(By.XPATH, "//textarea[@id='inputText1']")
input2 = driver.find_element(By.XPATH, "//textarea[@id='inputText2']")

input1.send_keys("welcome to selenium")

act = ActionChains(driver)

# Input1  crtl+A select text
# act.key_down(Keys.CONTROL).perform()
# act.send_keys("a").perform()
# act.key_up(Keys.CONTROL).perform()

# input1.send_keys(Keys.CONTROL,"a")  # without using actionchains class
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

# input1 crtl+c copy text
# act.key_down(Keys.CONTROL).perform()
# act.send_keys("c").perform()
# act.key_up(Keys.CONTROL).perform()

act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

# press tab key to navigate to input2
# act.send_keys(Keys.TAB)
# act.perform()

act.send_keys(Keys.TAB).perform()

# input2 -- crtl+v paste text
# act.key_down(Keys.CONTROL).perform()
# act.send_keys("v").perform()
# act.key_up(Keys.CONTROL).perform()

act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
