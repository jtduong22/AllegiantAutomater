# This file opens up and navigates through allegiantair.com
# will calculate and ensure the correct prices are listed

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from allegiant_config import option
from page_1 import *
from page_2 import *
from page_3 import *
from page_4 import *
from page_5 import *
from page_6 import *

def allegiant_automator(options: option):
    url = 'https://www.allegiantair.com/'

    result = False
    calculated_price = "Error"
    listed_price = "Error"
    error_message = ""

### options ###
    departure_location = options.departure_location
    destination_location = options.destination_location
    departure_date = options.departure_date
    return_date = options.return_date
    num_of_adults = options.num_of_adults
    bundle_type = options.bundle_type
    is_hotel_booked = options.is_hotel_booked
    is_car_booked = options.is_car_booked

    try:
        ## Load Webpage ##

        print(f"Attempting to load {url}")
        driver = webdriver.Firefox()
        driver.set_page_load_timeout(10)
        driver.implicitly_wait(10)
        driver.get(url)
        print('Load successful')

        wait = WebDriverWait(driver, 10)

        # keep track of prices
        all_costs = []

    ### PAGE 1 (Choose destination) ###
        parse_intro_page(driver, wait, departure_location, destination_location, departure_date[0], departure_date[1],
                         departure_date[2], return_date[0], return_date[1], return_date[2], num_of_adults)

    ### PAGE 2 (Get Flight prices) ###
        flight_cost = parse_flight_page(driver, wait)

    ### Page 3 (Bundle) ###
        bundle_cost = parse_bundle_page(driver, wait, bundle_type)

    ### Page 4 (Hotel) ###
        hotel_cost = parse_hotel_page(driver, wait, is_hotel_booked)

    ### Page 5 (Vehicle) ###
        car_cost = parse_car_page(driver, wait, is_car_booked)

    ### Page 6 ###
        if is_hotel_booked:
            all_costs = hotel_cost
        else:
            all_costs = flight_cost
        all_costs = (all_costs + bundle_cost) * num_of_adults + car_cost

        result, calculated_price, listed_price, error_message = compare_total_price(driver, wait, all_costs)

    except Exception as e:
        print(f"Type {type(e)} Exception has occurred: {e}")
        error_message = e

    # input("Press any button to continue . . .")
    driver.quit()
    return [result, calculated_price, listed_price, error_message]

