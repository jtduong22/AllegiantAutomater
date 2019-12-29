from selenium.common import exceptions as sel_exc
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

month_to_word = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}
word_to_month = {"January":1, "February":2, "March":3, "April":4, "May":5, "June":6, "July":7, "August":8, "September":9, "October":10, "November":11, "December":12}

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

def select_location(driver, location, is_return):
    flight_type = "Departure"
    if is_return == True:
        flight_type = "Destination"


    ## Select Location ##
    print(f"Searching for {flight_type} input")

    # find departure (from) box
    location_box = driver.find_element_by_name(f'search_form[{str.lower(flight_type)}_city]')
    print(f"{flight_type} Box found! Selecting {location}")

    # interact with box
    location_box.click()
    location_box.send_keys(location)
    time.sleep(1)
    location_box.send_keys(Keys.ENTER)

def select_date(driver, input_box, month, day, year):
    # find button and click
    print("Searching for Date Button")
    date_button = input_box.find_element_by_xpath('.//button')
    time.sleep(1)
    print("Button found! Clicking")
    date_button.click()

    # find current date to compare to selected
    current_month = driver.find_element_by_class_name("ui-datepicker-month").text
    current_year = int(driver.find_element_by_class_name("ui-datepicker-year").text)

    print("Checking date . . .")

    # while the year and month don't match, keep searching
    while not (word_to_month[current_month] == month and year == current_year):
        print(f"Current date is {current_month} {current_year} vs selected {month_to_word[month]} {year}")

        # year is too small or month is too small, increment page
        if current_year < year or (current_year == year and word_to_month[current_month] < month):
            # next page
            print("Moving to next page")
            time.sleep(.5)
            driver.find_element_by_partial_link_text("Next month").click()
        # shouldn't ever reach this point since you can't travel into the past
        else:
            # previous page
            print("Moving to previous page")
            time.sleep(.5)
            driver.find_element_by_partial_link_text("Previous month").click()

        # update which month and year the page is on
        current_month = driver.find_element_by_class_name("ui-datepicker-month").text
        current_year = int(driver.find_element_by_class_name("ui-datepicker-year").text)

    print("Found correct date!")

    # select date
    print(f"Selecting {month_to_word[month]} {day}")
    driver.find_element_by_id(f"ui-datepicker-0-{month-1}-{day}").click()

def parse_intro_page(driver, wait, departure_location, destination_location, dep_month = 1, dep_day = 26, dep_year = 2020, ret_month = 1, ret_day = 27, ret_year = 2020):
    ## Close popup ##
    clear_popup(driver, wait)

    ## Select Departure Location ##
    select_location(driver, departure_location, False)

    ## Select Destination Location ##
    select_location(driver, destination_location, True)

    ## Select Departure Date ##
    input_box = driver.find_element_by_name("search_form[departure_date]").find_element_by_xpath("..")
    select_date(driver, input_box, dep_month, dep_day, dep_year)

    ## Select Return Date ##
    input_box = driver.find_element_by_name("search_form[return_date]").find_element_by_xpath('..')
    select_date(driver, input_box, ret_month, ret_day, ret_year)

    ## Submit
    print("Moving on to the next page\n")
    driver.find_element_by_id("submit-search").click()