# This file opens up and navigates through allegiantair.com
# will calculate and ensure the correct prices are listed

from selenium import webdriver
from selenium.common import exceptions as sel_exc
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from page_1 import *
from page_2 import *
from page_3 import *
from page_4 import *
from page_5 import *
from page_6 import *

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
    # keep track of prices
    all_costs = []

### PAGE 1 ###
    departure_location = 'Bellingham, WA / Vancouver, BC (BLI)'
    destination_location = "Las Vegas, NV (LAS)"
    departure_date = [1,26,2020]
    return_date = [1,27,2020]
    num_of_adults = 3

    parse_intro_page(driver, wait, departure_location, destination_location, departure_date[0], departure_date[1],
                     departure_date[2], return_date[0], return_date[1], return_date[2], num_of_adults)

### PAGE 2 (Get Flight prices) ###
    all_costs += parse_flight_page(driver, wait) * num_of_adults

### Page 3 (Bundle) ###
    all_costs += parse_bundle_page(driver, wait)

### Page 4 (Hotel) ###
    all_costs += parse_hotel_page(driver, wait)

### Page 5 (Vehicle) ###
    all_costs += parse_car_page(driver, wait)

### Page 6 ###
    result = compare_total_price(driver, wait, all_costs)

except Exception as e:
    print(f"Type {type(e)} Exception has occurred: {e}")
    driver.quit()
    exit(1)


input("Press any button to continue . . .")
driver.quit()

