import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/gur31063/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
#action.context_click(driver.find_element(By.ID, id)) ##for right click
#action.double_click() -- for double click
#action.drag_and_drop(src,target)
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
#always add perform if using ActionChain class
#action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()

action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()
time.sleep(2)