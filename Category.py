from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.binary_location = GOOGLE_CHROME_PATH

with webdriver.Chrome(execution_path=CHROMEDRIVER_PATH, chrome_options=chrome_options) as driver:
    wait = WebDriverWait(driver, 10)
    driver.get(base_url + url)
    first_result = wait.until(presence_of_element_located((By.CLASS_NAME, "clickable-category")))
    category = first_result.get_attribute("textContent")
    driver.quit
print(category)
