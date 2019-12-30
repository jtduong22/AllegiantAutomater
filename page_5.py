from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

def parse_car_page(driver, wait, is_car_booked):
    car_price = '0.00'

    # book car if true
    if is_car_booked:
        # wait for page to complete loading
        print("Waiting for page to load. . .")
        wait.until(ec.presence_of_element_located((By.ID, "vehicles")))

        # select first car
        print("Loaded. Selecting first car")
        car_chooser = driver.find_element_by_id("vendors")
        car_listing = car_chooser.find_element_by_xpath(".//div[2]/table/tbody/tr[1]/td[1]/span/a")

        print("Car selected. Getting price")
        # get car price
        car_price = ''.join(x for x in car_listing.text if str.isnumeric(x) or x == '.')
        car_listing.click()

        print("Waiting until price updates. . . ")
        wait.until(ec.staleness_of(car_chooser))

    print(f"added car price is ${car_price}")

    # Wait until button is enabled
    wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='transport']//div[3]/div/button")))

    print("Moving onto the next page\n")
    driver.find_element_by_id("transport").find_element_by_xpath(".//div[3]/div/button").click()

    return [car_price]