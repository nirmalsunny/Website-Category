from flask import Flask
from flask import request, Response
from flask import render_template
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'

mitphish = Flask(__name__)

@mitphish.route('/')
def homepage():
    return "MitPhish" #+ path Yay, the file exists! 


mitphish.route('/test/<path:path>')
def show_index(path):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.binary_location = GOOGLE_CHROME_PATH

    with webdriver.Chrome(execution_path=CHROMEDRIVER_PATH, chrome_options=chrome_options) as driver:
        wait = WebDriverWait(driver, 10)
        driver.get(base_url + path)
        first_result = wait.until(presence_of_element_located((By.CLASS_NAME, "clickable-category")))
        category = first_result.get_attribute("textContent")
        driver.quit
   return category

if __name__ == "__main__":
    mitphish.run(debug=True, threaded=True, port = int(os.environ.get('PORT', 5000)))
