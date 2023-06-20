from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:/Users/gur31063/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

##for Firefox use ->
# service_obj = Service(download geckodriver)
# driver = webdriver.Firefox(service=service_obj)

##for Edge use ->
# service_obj = Service(download ms edge driver)
# driver = webdriver.Edge(service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
#driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()