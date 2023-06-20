import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList =[]
service_obj = Service("C:/Users/gur31063/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(2)
#5 seconds is max time out. if process completed n 2 secs it saves 3 secs
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
prdtcs = driver.find_elements(By.XPATH, "//div[@Class='products']/div")
print(len(prdtcs))
for prdct in prdtcs:
    actualList.append(prdct.find_element(By.XPATH, "h4").text)

assert expectedList == actualList

