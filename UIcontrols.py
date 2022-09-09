from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Users\\Admin\\Desktop\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")

print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value")== "option2":
        checkbox.click()
        assert checkbox.is_selected()

        break

RadioButton = driver.find_elements(By.XPATH,"//input[@type='radio']")

for Radio in RadioButton:
    if Radio.get_attribute("value") == " radio2":
        Radio.click()

        assert Radio.is_selected()


        break