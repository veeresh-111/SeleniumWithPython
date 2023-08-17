import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import mysql.connector

serv_obj = Service("C:\WebDrivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()
try:
    con = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="vskroot", database="mydb")
    curs = con.cursor()  # create curser for temparary memory
    curs.execute("select * from caldata")  # execute query through curser

    for row in curs:
        # read data from database table caldata
        pric = row[0]
        rateofinterest = row[1]
        per1 = row[2]
        pre2 = row[3]
        fre = row[4]
        exp_mvalue = row[5]

        # passing data into application
        driver.find_element(By.XPATH, "//input[@id='principal']").send_keys(pric)
        driver.find_element(By.XPATH, "//input[@id='interest']").send_keys(rateofinterest)
        driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(per1)
        perioddrp = Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']"))
        perioddrp.select_by_visible_text(pre2)
        frequencydrp = Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
        frequencydrp.select_by_visible_text(fre)
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[1]/img").click()  # calculate button

        act_mvalue = driver.find_element(By.XPATH, "//span[@id='resp_matval']/strong").text  # get actual calculated maturevalue

        # Validation
        if float(exp_mvalue) == float(act_mvalue):
            print("test passed")
        else:
            print("test failed")

        driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[2]/img").click() # clear all entered one iteration data
        time.sleep(3)
    con.close()
except:
    print("Connection UnSuccessful....")

driver.close()

