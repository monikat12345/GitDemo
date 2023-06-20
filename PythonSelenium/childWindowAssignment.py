import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/gur31063/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()
time.sleep(3)

openedwindows = driver.window_handles
driver.switch_to.window(openedwindows[1])

#driver.find_element(By.XPATH, "//h3")
#driver.find_element(By.CSS_SELECTOR, "h3")
mailid = driver.find_element(By.XPATH, "//p[@Class='im-para red']/strong").text

driver.close()
driver.switch_to.window(openedwindows[0])
driver.find_element(By.ID, "username").send_keys(mailid)
driver.find_element(By.ID, "password").send_keys("12345")
driver.find_element(By.ID, "signInBtn").click()
