from selenium.common import exceptions as sel_exc
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

def clear_popup(driver, wait):
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

def intro_page(driver, wait):
    clear_popup(driver, wait)    ## Close popup ##

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

    ## Select Departure Date ##

    print("Searching for Departure Date Button")
    date_button = driver.find_element_by_class_name("datepicker-toggle")
    time.sleep(1)
    print("Button found! Clicking")
    date_button.click()

    # next page
    print("Moving to next page")
    time.sleep(.5)
    driver.find_element_by_partial_link_text("Next month").click()

    # select date
    print("Selecting January 26th")
    driver.find_element_by_id("ui-datepicker-0-0-26").click()

    ## Select Return Date ##

    print("Searching for Return Date Button")
    date_button = driver.find_element_by_xpath(
        "/html/body/div[5]/div/div/div[1]/div[1]/div/div[2]/div[1]/div/div/div[1]/form/div/div[1]/div[2]/div[2]/div/div/div/button")
    time.sleep(1)
    print("Button found! Clicking")
    date_button.click()

    # select date
    print("Selecting January 27th")
    driver.find_element_by_id("ui-datepicker-0-0-27").click()

    ## Submit
    driver.find_element_by_id("submit-search").click()