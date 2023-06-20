#####execute java script
##taking screen shot
###head less mode , means browser runs at backend
import time

from selenium import webdriver
#from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")

#to handle certificates messages
chrome_options.add_argument("--ignore-certificate-errors")


service_obj = Service("C:/Users/gur31063/chromedriver_win32/chromedriver.exe")
#driver = webdriver.Chrome(service=service_obj)
#for headless do as below
driver = webdriver.Chrome(service=service_obj,options=chrome_options)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
#driver.execute_script("window.scrollBy(0,window.scrollBy(0,500);")
time.sleep(2)
driver.get_screenshot_as_file("screen2.png")
