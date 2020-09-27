from flask import Flask
from flask import request, Response
from flask import render_template
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import os


wc = Flask(__name__)


@wc.route('/')
def homepage():
    return "MitPhish"  # + path Yay, the file exists!


@wc.route('/check/<path:url>')


def show_index(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--remote-debugging-port=9222')
    chrome_options.binary_location = str(os.environ.get(GOOGLE_CHROME_BIN))

    with webdriver.Chrome(executable_path=str(os.environ.get(CHROMEDRIVER_PATH)), chrome_options=chrome_options) as driver:
        wait = WebDriverWait(driver, 10)
        driver.get(base_url + url)
        first_result = wait.until(presence_of_element_located((By.CLASS_NAME, "clickable-category")))
        category = first_result.get_attribute('textContent')
        driver.quit
    return category


port = int(os.environ.get('PORT', 5000))

if __name__ == "__main__":
    wc.run(debug=True, threaded=True, port=port)
