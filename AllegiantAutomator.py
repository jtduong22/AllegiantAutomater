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

### PAGE 1 ###
    departure_location = 'Bellingham, WA / Vancouver, BC (BLI)'
    destination_location = "Las Vegas, NV (LAS)"
    departure_date = [1,26,2020]
    return_date = [1,27,2020]

    parse_intro_page(driver, wait, departure_location, destination_location, departure_date[0], departure_date[1], departure_date[2], return_date[0], return_date[1], return_date[2])
### PAGE 2 ###
    parse_flight_page(driver, wait)


### Page 3 ###
    bundle_price = '0.00'

    print(f"added bundle price is ${bundle_price}")

    # Wait until button is enabled
    wait.until(ec.element_to_be_clickable((By.CLASS_NAME, "continue")))
    print("Moving onto the next page\n")
    driver.find_element_by_class_name("continue").click()

### Page 4 ###
    hotel_price = '0.00'

    print(f"added hotel price is ${hotel_price}")

    # Wait until button is enabled
    wait.until(ec.element_to_be_clickable((By.CLASS_NAME, "continue")))
    print("Moving onto the next page\n")
    driver.find_element_by_class_name("continue").click()

### Page 5 (Vehicle) ###
    car_price = '0.00'

    print(f"added car price is ${car_price}")

    # Wait until button is enabled
    wait.until(ec.element_to_be_clickable((By.CLASS_NAME, "continue")))
    print("Moving onto the next page\n")
    driver.find_element_by_class_name("continue").click()

except Exception as e:
    print(f"Type {type(e)} Exception has occurred: {e}")
    driver.quit()
    exit(1)


input("Press any button to continue . . .")
driver.quit()

