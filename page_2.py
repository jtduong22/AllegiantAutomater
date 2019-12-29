from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

def get_price(driver, is_return):
    flight_type = "departing"
    if is_return:
        flight_type = "returning"

    # get all radio buttons
    radio_query = driver.find_element_by_id(f"{flight_type}").find_elements_by_name(f"{flight_type}-flight")
    radio_button = None

    # find which radio_button is selected
    for button in radio_query:
        if button.is_selected() == True:
            print("Found selected radio button! Continuing...")
            radio_button = button
            break

    # failsafe if none are selected
    if radio_button == None:
        raise Exception("No radio button selected???")

    print("Finding price of flight...")
    parent = radio_button.find_element_by_xpath('../../..')

    # select the object containing the price
    p_span = parent.find_element_by_xpath('.//span[2]/span/span[3]')
    prices = p_span.text.split()

    # get last element (so it ignores strikethrough price if doing round trip)
    price = prices[len(prices) - 1]
    price = price[1:len(price)]  # get rid of dollar sign
    return price

def parse_flight_page(driver, wait):
    # Wait for page to load
    print("Waiting for page to load . . .")
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "calendar")))
    print("Done loading! Looking for selected element")

    ## Get price of departure flight
    dep_price = get_price(driver, False)
    print(f"The price is ${dep_price}")

    ## Get price of Return flight
    ret_price = get_price(driver, True)
    print(f"The price is ${ret_price}")

    ## Continue on to next page
    print("Moving on to the next page\n")
    button = driver.find_element_by_class_name("button-wrapper").find_element_by_tag_name("button")
    button.click()