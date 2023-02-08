#scraping dynamiczny UwU desune kawaii kya >////<

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
url = 'https://www.reddit.com/r/ChuckNorris/'
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")
driver = webdriver.Chrome(executable_path = DRIVER_BIN, options=options)

driver.get(url)

#button = WebDriverWait(driver,10).until(prsc("selector"))

#element_list = driver.find_elements(By.CSS_SELECTOR, 'h2, h2 + div')
#for element in element_list:
#    print(element.text)


#input('Press ENTER to close the automated browser')
#driver.quit()

driver.close()

