from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Users\\Admin\\Desktop\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(3)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
driver.find_element(By.CLASS_NAME,"blinkingText").click()

Window = driver.window_handles
driver.switch_to.window(Window[1])
Copied = (driver.find_element(By.XPATH,"//p[@class = 'im-para red']").text)
Split = Copied.split()
GrabText = Split[4]
driver.close()

driver.switch_to.window(Window[0])
driver.find_element(By.ID,"username").send_keys(GrabText)
driver.find_element(By.ID,"password").send_keys("Atif@123")
driver.find_element(By.XPATH,"//input[@type = 'password']")
driver.find_element(By.ID,"signInBtn").click()
alert = driver.find_element(By.XPATH,"//div[@style = 'display: block;']").text
print(alert)