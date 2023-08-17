import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

location = os.getcwd()

# Chrome browser
def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:\WebDrivers\chromedriver.exe")

    # Download file in desired location
    preferences = {"download.default_directory":location, "plugins.always_open_pdf_externally":True}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", preferences)

    driver = webdriver.Chrome(service=serv_obj, options=ops)
    return driver

#Edge browser
def edge_setup():
    from selenium.webdriver.edge.service import Service
    serv_obj = Service("C:\WebDrivers\msedgedriver.exe")

    #Download file in desired location
    preferences = {"download.default_directory":location, "plugins.always_open_pdf_externally":True}
    ops = webdriver.EdgeOptions()
    ops.add_experimental_option("prefs", preferences)

    driver = webdriver.Edge(service=serv_obj, options=ops)
    return driver

#Firefox browser
def firefox_setup():
    from selenium.webdriver.firefox.service import Service
    serv_obj = Service("C:\WebDrivers\geckodriver.exe")
    #settinfs
    ops=webdriver.FirefoxOptions()
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk","application/pdf")
    ops.set_preference("browser.download.manager.showWhenStarting", False)
    ops.set_preference("browser.download.folderList",2) #0-desktop 1-download folder, 2-Desired location
    ops.set_preference("browser.download.dir",location)
    ops.set_preference("pdfjs.disabled",True)  # for pdf file only

    driver = webdriver.Firefox(service=serv_obj, options=ops)
    return driver


#Automated code
# driver = chrome_setup()
# driver = edge_setup()
driver = firefox_setup()

driver.implicitly_wait(10)
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/")
driver.maximize_window()

driver.find_element(By.XPATH, "//tbody/tr[1]/td[5]/a[1]").click()

print("Done--------")
