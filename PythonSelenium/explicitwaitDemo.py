import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:/Users/gur31063/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(2)
#5 seconds is max time out. if process completed n 2 secs it saves 3 secs
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
driver.find_elements(By.XPATH, "//div[@Class='products']/div/products/product-name")

results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0
time.sleep(2)
for result in results:
    result.find_element(By.XPATH, "div/button").click()

time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

#sum validation
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sums = 0
for price in prices:
    sums = sums + int(price.text)

print(sums)
totalamt = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

assert sums == totalamt

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
#time.sleep(5)
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

discamt = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)

print(discamt)

assert totalamt > discamt
