import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

name = "Hi"

service_obj = Service("C:/Users/gur31063/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alerttext = alert.text
print(alerttext)
#assert "Go" in alerttext
assert name in alerttext
alert.accept()
#alert.dismiss()