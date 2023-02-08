from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.expected_conditions import presence_of_element_located as prsc
from selenium.webdriver.support.wait import WebDriverWait
import os
import time

options = Options()
#options.add_argument('--headless')
options.add_argument('--disable-notifications')
options.add_argument('--disable-notifications')

DRIVER_PATH = '/Users/adamignaciuk/Desktop/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://google.com')


driver.close()


