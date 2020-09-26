from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located


# This import is needed only when you run this file in isolation.
import sys


geckodriver = 'path/to/geckodriver'

def sitereview(url): 
    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')
    base_url = "https://sitereview.bluecoat.com/#/lookup-result/"
    
    with webdriver.Firefox(executable_path=geckodriver, options=options) as driver:
        wait = WebDriverWait(driver, 10)
        driver.get(base_url + url)
        first_result = wait.until(presence_of_element_located((By.CLASS_NAME, "clickable-category")))
        category = first_result.get_attribute("textContent")
        driver.quit
    return category   

def main(url):
    border = "=" * (len("Website Category") + 2)
    print("\n{0}\n{1}\n{0}\n".format(border, "Website Category"))
    print("URL: " + url)
    print("Category: " + sitereview(url))

# Use the below two lines if website_category.py is being run as a standalone file. If you are running this file as
# a part of a workflow pipeline, comment out these two lines.
if __name__ == "__main__":
    if len(sys.argv) != 2:
         print("Please use the following format for the command - `python website_category.py <url-to-be-checked>`")
         exit(0)
    main(sys.argv[1])
