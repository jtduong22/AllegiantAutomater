# This file opens up and navigates through allegiantair.com
# will calculate and ensure the correct prices are listed

from selenium import webdriver
from selenium.common import exceptions as sel_exc
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
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
    date_button = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div[1]/div/div[2]/div[1]/div/div/div[1]/form/div/div[1]/div[2]/div[2]/div/div/div/button")
    time.sleep(1)
    print("Button found! Clicking")
    date_button.click()

    # select date
    print("Selecting January 27th")
    driver.find_element_by_id("ui-datepicker-0-0-27").click()

    ## Submit
    driver.find_element_by_id("submit-search").click()

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

