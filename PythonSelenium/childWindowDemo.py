import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/gur31063/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()

openedwindows = driver.window_handles
driver.switch_to.window(openedwindows[1])

#driver.find_element(By.XPATH, "//h3")
#driver.find_element(By.CSS_SELECTOR, "h3")
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close()
time.sleep(2)
driver.switch_to.window(openedwindows[0])
print(driver.find_element(By.TAG_NAME, "h3").text)