from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

def parse_flight_page(driver, wait):
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
    dep_price = price[1:len(price)]  # get rid of dollar sign
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