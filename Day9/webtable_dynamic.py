import time
from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\WebDrivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)


driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
driver.implicitly_wait(10)

#Login
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()

# Admin ----> User management -----> users
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click()
driver.find_element(By.XPATH,"//span[normalize-space()='User Management']").click()
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li/a").click()


# total rows in a table
rows=len(driver.find_elements(By.XPATH,"//div[@class='oxd-table-body']/div"))
print("Total number of rows in a table:",rows)

count=0
for r in range(1,rows+1):
    status=driver.find_element(By.XPATH,"//div[@class='oxd-table-body']/div["+str(r)+"]/div/div[5]").text
    if status=='Enabled':
        count=count+1

print("Total number of users:",rows)
print("Number of Enabled user:",count)
print("Number of disabled user:",(rows-count))


driver.close()