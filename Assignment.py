import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


Veg_List = ['Cucumber - 1 Kg' , 'Raspberry - 1/4 Kg' , 'Strawberry - 1/4 Kg']
Actual_List = []

service_obj = Service("C:\\Users\\Admin\\Desktop\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element(By.CLASS_NAME, "search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class ='products']/div")
count = len(results)
print(count)
assert count > 0
for result in results:
    result.find_element(By.XPATH,"div/button").click()

Vegies = driver.find_elements(By.XPATH,"//h4[@class='product-name']")
for Veg in Vegies:
    Actual_List.append(Veg.text)
print(Actual_List)

driver.find_element(By.XPATH,"//img[@alt = 'Cart']").click()
driver.find_element(By.XPATH,"//button[@type = 'button']").click()

prices = driver.find_elements(By.XPATH,"//td[5]/p")
sum = 0
for price in prices:
    sum = sum + int(price.text)


driver.find_element(By.CLASS_NAME,"promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME,'promoBtn').click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoInfo")))
TotalAmt = int(driver.find_element(By.CLASS_NAME,"totAmt").text)
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)
DisAmt = float(driver.find_element(By.CLASS_NAME,"discountAmt").text)

assert sum == TotalAmt
assert DisAmt < TotalAmt
assert Veg_List == Actual_List




