from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
from selenium.common.exceptions import NoSuchElementException
from rich import print as rprint
from rich.console import Console

def scrape_movies(driver, search):

    options = Options()

    options.add_argument("--disable-cookies")

    driver = webdriver.Chrome(options=options)

    driver.get('https://www.youtube.com')
    driver.maximize_window()
    time.sleep(10)
    driver.find_element(By.XPATH,'//*[@id="content"]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button').click()
    time.sleep(5)

    #time.sleep(10)
    #driver.find_element(By.NAME,"agreeButton").click()
    #driver.find_element(By.CSS_SELECTOR("agreeButton")).click()
    #try:
    #    frame = driver.find_element(By.XPATH,'//*[@id="cnsw"]/iframe')  # <-locating chrome cookies consent frame
    #    driver.switch_to.frame(frame)
    #    driver.find_element(By.XPATH,'//*[@id="content"]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button').click()
    #except NoSuchElementException:
    #    driver.find_element(By.XPATH, '//*[@id="L2AGLb"]').click()  # <- pay attention to new id.
    #driver.find_element(By.XPATH, '//*[@id="uc-btn-accept-banner"]').click()
    time.sleep(10)
  #Scroll through the page
    SCROLL_PAUSE_TIME = 2
    # Get the list of all open windows

    #last_height = driver.execute_script("return document.body.scrollHeight")
    time.sleep(5)
    search_bar = driver.find_element(By.NAME,'search_query')
    # Click on the search bar
    search_bar.click()
    search_bar.send_keys(search)
    search_bar.submit()
    movies = []
    for i in range(2):
        driver.execute_script("window.scrollBy(0, window.innerHeight);")
        time.sleep(2)
        titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')
        movies.append([title.text for title in titles])
    #wait = WebDriverWait(driver, 10)


   # movies = [title.text for title in titles]

    return movies



driver = webdriver.Chrome()
time.sleep(5)

search = "Fiber Bragg Grating"
movies = scrape_movies(driver,search)

#print(movies)

driver.quit()

console = Console()
rprint(movies)



