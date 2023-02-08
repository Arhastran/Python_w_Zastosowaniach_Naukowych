from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

def scrape_movies(driver):
    # Create an instance of ChromeOptions
    options = Options()
    # Add the --disable-cookies argument
    options.add_argument("--disable-cookies")
    # Start the Chrome browser
    driver = webdriver.Chrome(options=options)
    # Navigate to the YouTube main page
    driver.get("https://www.youtube.com")
    driver.maximize_window()
    driver.find_element(By.XPATH, '//*[@id="uc-btn-accept-banner"]').click()
  #Scroll through the page
    SCROLL_PAUSE_TIME = 2
    # Get the list of all open windows

    last_height = driver.execute_script("return document.body.scrollHeight")
    time.sleep(5)
    search_bar = driver.find_element(By.NAME,'search_query')
    # Click on the search bar
    search_bar.click()
    search_bar.send_keys("Warhammer 40k")
    search_bar.submit()

    while True:
        # Scroll down to the bottom of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait for the page to load
        wait = WebDriverWait(driver, SCROLL_PAUSE_TIME)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".ytd-watch-next-secondary-results-renderer")))

        # Calculate the new height of the page
        new_height = driver.execute_script("return document.body.scrollHeight")

        # If the new height is the same as the last height, it means that the page has finished loading
        if new_height == last_height:
            break

        # Update the last height
        last_height = new_height


    #wait = WebDriverWait(driver, 10)
    titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')

    # Extract the movie titles
    movies = [title.text for title in titles]

    # Return the movie titles
    return movies


# Start the Chrome browser
driver = webdriver.Chrome()
time.sleep(5)
# Call the scrape_movies function

movies = scrape_movies(driver)

# Print the movie titles
print(movies)

# Close the browser
driver.quit()



