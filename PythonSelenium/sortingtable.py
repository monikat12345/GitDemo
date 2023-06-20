import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
browsersortedveggies = []
service_obj = Service("C:/Users/gur31063/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
#click on column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
#collect all vegie list
veggiewebelements = driver.find_elements(By.XPATH, "//tr/td[1]")
for veggies in veggiewebelements:
    browsersortedveggies.append(veggies.text)
originalbrowsersortedlist = browsersortedveggies.copy()
#sort vegie list - new sorted list
browsersortedveggies.sort()

assert browsersortedveggies == originalbrowsersortedlist