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

    intro_page(driver, wait, departure_location, destination_location, departure_date[0], departure_date[1],departure_date[2], return_date[0],return_date[1], return_date[2])
### PAGE 2 ###

    ## Get price of departure flight

    print("Waiting for page to load . . .")
    # time.sleep(7)
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "calendar")))

    print("Done loading! Looking for selected element")

    radio_query = driver.find_element_by_id("departing").find_elements_by_name("departing-flight")
    radio_button = None

    for button in radio_query:
        print(button.tag_name, ' ', button.is_selected(), ' ', type(button.is_selected()))
        if button.is_selected() == True:
            print("Found selected radio button! Continuing...")
            radio_button = button
            break

    if radio_button == None:
        raise Exception("No radio button selected???")
    # radio_button = driver.find_element_by_name("departing-flight")

    print("Finding price of flight...")
    parent = radio_button.find_element_by_xpath('../../..')

    # select the object containing the price
    p_span = parent.find_element_by_xpath('.//span[2]/span/span[3]')
    prices = p_span.text.split()

    # get last price (ignores strike through price if doing round trip)
    price = prices[len(prices) - 1]
    dep_price = price[1:len(price)]   # get rid of dollar sign
    print(f"The price is ${dep_price}")

    ## Get price of Return flight

    print("Looking for Return flight! Looking for selected element")

    radio_query = driver.find_element_by_id("returning").find_elements_by_name("returning-flight")
    radio_button = None

    for button in radio_query:
        print(button.tag_name, ' ', button.is_selected(), ' ', type(button.is_selected()))
        if button.is_selected() == True:
            print("Found selected radio button! Continuing...")
            radio_button = button
            break

    if radio_button == None:
        raise Exception("No radio button selected???")
    # radio_button = driver.find_element_by_name("departing-flight")

    print("Finding price of flight...")
    parent = radio_button.find_element_by_xpath('../../..')

    # select the object containing the price
    p_span = parent.find_element_by_xpath('.//span[2]/span/span[3]')
    prices = p_span.text.split()

    # get last price (ignores strike through price if doing round trip)
    price = prices[len(prices) - 1]
    ret_price = price[1:len(price)]  # get rid of dollar sign
    print(f"The price is ${ret_price}")

    ## Continue on to next page
    # driver.find_element_by_class_name("continue enabled").click()
    button = driver.find_element_by_class_name("button-wrapper").find_element_by_tag_name("button")
    button.click()


### Page 3 ###
    bundle_price = '0.00'

    print(f"added bundle price is ${bundle_price}")

    # Wait until button is enabled
    wait.until(ec.element_to_be_clickable((By.CLASS_NAME, "continue")))
    print("moving onto next page")
    driver.find_element_by_class_name("continue").click()

### Page 4 ###
    hotel_price = '0.00'

    print(f"added hotel price is ${hotel_price}")

    # Wait until button is enabled
    wait.until(ec.element_to_be_clickable((By.CLASS_NAME, "continue")))
    print("moving onto next page")
    driver.find_element_by_class_name("continue").click()

### Page 5 (Vehicle) ###
    car_price = '0.00'

    print(f"added car price is ${car_price}")

    # Wait until button is enabled
    wait.until(ec.element_to_be_clickable((By.CLASS_NAME, "continue")))
    print("moving onto next page")
    driver.find_element_by_class_name("continue").click()

except Exception as e:
    print(f"Type {type(e)} Exception has occurred: {e}")
    driver.quit()
    exit(1)


input("Press any button to continue . . .")
driver.quit()

