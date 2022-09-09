from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:\\Users\\Admin\\Desktop\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(3)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
Products = driver.find_elements(By.XPATH,"//div[@class='card h-100']")


for Product in Products:
    Productname = Product.find_element(By.XPATH, "div/h4/a").text
    if Productname == "Blackberry":
        Product.find_element(By.XPATH,"div/button").click()

driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()



driver.find_element(By.ID,"country").send_keys("Ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.XPATH,"//label[@for='checkbox2']").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
Success = (driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text)

assert "Success! Thank you!" in Success
driver.close()