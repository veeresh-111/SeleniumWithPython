from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\WebDrivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()
countrylist=driver.find_elements(By.XPATH,"//ul[@id='select2-billing_country-results']/li")
print(len(countrylist))  # 249

for country in countrylist:
    if country.text=="India":
        country.click()
        break
