from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Users\\Admin\\Desktop\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.find_element(By.ID,"name").send_keys("Atif")
driver.find_element(By.ID,"confirmbtn").click()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()



