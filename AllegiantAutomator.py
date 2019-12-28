# This file opens up and navigates through allegiantair.com
# will calculate and ensure the correct prices are listed

from selenium import webdriver
from selenium.common import exceptions as sel_exc
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
url = 'https://www.allegiantair.com/'

## Load Webpage ##

print(f"Attempting to load {url}")
driver = webdriver.Firefox()
driver.set_page_load_timeout(10)
driver.implicitly_wait(10)
driver.get(url)
print('Load successful')

wait = WebDriverWait(driver, 10)

try:

    ## Close popup ##
    try:
        print("Waiting for credit card popup . . .")

        # Wait until popup

        wait.until(ec.visibility_of(driver.find_element_by_class_name("credit-card-overlay-content")))
        popup = driver.find_element_by_class_name("credit-card-overlay-content")
        print("Popup found! Closing popup. . .")

        time.sleep(1)

        # Press Escape Button to close popup

        actions = ActionChains(driver)
        actions.send_keys(Keys.ESCAPE)
        actions.send_keys(Keys.ESCAPE)
        actions.send_keys(Keys.ESCAPE)
        actions.perform()

        # wait.until(ec.invisibility_of_element_located(popup))
        print("Closed popup!")
        # wait.until(ec.invisibility_of_element(driver.find_element_by_class_name("credit-card-overlay-content")))


    # No popup found, continue with program
    except sel_exc.NoSuchElementException:
        print("No Popup found, continuing. . . ")

    ## Select Departure Location ##
    print("Searching for Departure input")
    dep_location = 'Bellingham, WA / Vancouver, BC (BLI)'

    # find departure (from) box
    dep_box = driver.find_element_by_name('search_form[departure_city]')
    print(f"Departure Box found! Selecting {dep_location}")

    # interact with box
    dep_box.click()
    dep_box.send_keys(dep_location)
    time.sleep(1)
    dep_box.send_keys(Keys.ENTER)

    ## Select Destination Location ##

    print("Searching for Destination input")
    des_location = "Las Vegas, NV (LAS)"

    # find destination (to) box
    des_box = driver.find_element_by_name("search_form[destination_city]")
    print(f"Destination Box found! Selecting {des_location}")

    # interact with box
    des_box.click()
    des_box.send_keys(des_location)
    time.sleep(1)
    des_box.send_keys(Keys.ENTER)

except Exception as e:
    print(f"Type {type(e)} Exception has occurred: {e}")
    driver.quit()
    exit(1)


input("Press any button to continue . . .")
driver.quit()

