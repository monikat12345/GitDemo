import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

browsersortedveggies = []
service_obj = Service("C:/Users/gur31063/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice/")
#driver.find_element(By.LINK_TEXT, "a[href='/angularpractice/shop']").click()
driver.find_element(By.XPATH, "//a[@href='/angularpractice/shop']").click()
# //a[contains(@href, 'shop')]
products = driver.find_elements(By.XPATH, "//div[@Class='card h-100']")
for product in products:
    #print(product.text)
    prodName = product.find_element(By.XPATH, "div/h4/a").text
    if prodName == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()
        break
driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
time.sleep(5)

driver.find_element(By.XPATH, "//button[@Class='btn btn-success']").click()
driver.find_element(By.ID, "country").send_keys("ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.XPATH, "//div[@Class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
successtext = driver.find_element(By.CLASS_NAME, "alert-success").text
assert "Success! Thank you!" in successtext
print(successtext)
driver.close()
