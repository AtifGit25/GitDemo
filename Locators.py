from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:\\Users\\Admin\\Desktop\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.CSS_SELECTOR,"input[name= 'name']").send_keys("Atif Inamdar")
driver.find_element(By.NAME,"email").send_keys("Inamdar.atif@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("123")

dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_index(0)
dropdown.select_by_visible_text("Female")




driver.find_element(By.ID,"exampleCheck1").click()
driver.find_element(By.XPATH,"//input[@type = 'submit']").click()

message = driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
assert "Success" in message

driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()