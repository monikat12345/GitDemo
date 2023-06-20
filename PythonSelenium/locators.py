import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:/Users/gur31063/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")

#different locators selenium provides ID, xpath, CSSSelector, Classname, name , linkText
driver.find_element(By.NAME, "email").send_keys("mymail@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.maximize_window()
driver.find_element(By.ID, "exampleCheck1").click()


# XPath - //tagname[@attribute='value'] //input[@type='submit']
#CSS - tagname[attribute='value'] input[type='submit'], #id , .classname
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Great")
driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()

###static dropdown

dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_index(0)
time.sleep(5)
dropdown.select_by_visible_text("Female")
#dropdown.select_by_value("provide value")- if value is present

driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text

print(message)

assert "success" in message
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Day")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
time.sleep(20)

driver.close()
