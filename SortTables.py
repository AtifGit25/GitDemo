from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Users\\Admin\\Desktop\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(3)

BrowserVegList = []
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()
driver.find_element(By.XPATH,"//th[@role = 'columnheader']").click()
BrowserVeg = driver.find_elements(By.XPATH,"//tr/td[1]")

for ele in BrowserVeg:
    BrowserVegList.append(ele.text)

    OriginalList = BrowserVegList.copy()

BrowserVegList.sort()

assert BrowserVegList == OriginalList

print(OriginalList)
print(BrowserVegList)