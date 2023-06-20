import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/gur31063/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))
time.sleep(1)
for country in countries:
    if country.text == "India":
        country.click()
        break
time.sleep(2)

#print(driver.find_element(By.ID, "autosuggest").text) - to get getting preloaded value
#print(driver.find_element(By.ID, "autosuggest").get_attribute("value")) - to get value provided by automation

assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "IndiaG"



