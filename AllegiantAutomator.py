# This file opens up and navigates through allegiantair.com
# will calculate and ensure the correct prices are listed

from selenium import webdriver
from selenium.common import exceptions as sel_exc
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
url = 'https://www.allegiantair.com/'

## Load Webpage ##

print(f"Attempting to load {url}")
driver = webdriver.Firefox()
driver.set_page_load_timeout(10)
driver.implicitly_wait(10)
driver.get(url)
print('Load successful')

try:
    try:
        print("Waiting for credit card popup . . .")
        # Wait until popup

        wait = WebDriverWait(driver, 10)
        wait.until(ec.visibility_of(driver.find_element_by_class_name("credit-card-overlay-content")))

        print("Popup found! Closing popup. . .")

        # Press Escape Button to close popup

        actions = ActionChains(driver)
        actions.send_keys(Keys.ESCAPE)
        actions.perform()

    # No popup found, continue with program
    except sel_exc.NoSuchElementException:
        print("No Popup found, continuing. . . ")


except Exception as e:
    print(f"Type {type(e)} Exception has occured: {e}")

input("Press any button to continue . . .")
driver.close()

