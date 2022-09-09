import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#service_obj = Service("C:\\Users\\Admin\\Desktop\\chromedriver.exe")
#driver = webdriver.Chrome(service=service_obj)

#service_obj = Service("C:\\Users\\Admin\\Desktop\\geckodriver.exe")
#driver = webdriver.Firefox(service=service_obj)

service_obj = Service("C:\\Users\\Admin\\Desktop\\msedgedriver.exe")
driver = webdriver.Edge(service=service_obj)


driver.maximize_window()
driver.get("https://rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.minimize_window()
driver.back()
driver.forward()
driver.refresh()
driver.close()
