from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\WebDrivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# capture cookies from the browser
cookies=driver.get_cookies()
print("Size of cookies:",len(cookies))  # 5

# print dateils of  all cookies
# for c in cookies:
#     #print(c)
#     print(c.get('name'),":",c.get('value'))

# Add new cookie to browser
driver.add_cookie({"name":"MyCookie", "value":"123456"})
cookies=driver.get_cookies()
print("Size of cookies after adding new one:",len(cookies))  # 6

# Delete specific cookie from the browser
driver.delete_cookie("MyCookie")
cookies=driver.get_cookies()
print("Size of cookies after deleted one:",len(cookies))  # 5

# Delete all the cookies
driver.delete_all_cookies()
cookies=driver.get_cookies()
print("Size of cookies after deleted all:",len(cookies))  # 0

driver.quit()