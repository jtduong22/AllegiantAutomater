from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

def parse_car_page(driver, wait, is_car_booked):
    car_price = '0.00'

    if is_car_booked:
        print("Waiting for page to load. . .")
        wait.until(ec.presence_of_element_located((By.ID, "vehicles")))

        print("Loaded. Selecting first car")
        car_chooser = driver.find_element_by_id("vendors")
        car_listing = car_chooser.find_element_by_xpath(".//div[2]/table/tbody/tr[1]/td[1]/span/a")

        car_price = ''.join(x for x in car_listing.text if str.isnumeric(x) or x == '.')
        car_listing.click()

    print(f"added car price is ${car_price}")

    # Wait until button is enabled
    # wait.until(ec.presence_of_element_located((By.ID, "vehicles")))
    # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, "white-overlay")))
    # wait.until_not(ec.visibility_of_element_located((By.CLASS_NAME, "white-overlay")))
    # wait.until(ec.element_to_be_clickable((By.CLASS_NAME, "continue")))
    # wait.until(ec.element_to_be_clickable(driver.find_element_by_id("transport").find_elements_by_xpath(".//div[3]/div/button")))
    wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='transport']//div[3]/div/button")))

    print("Moving onto the next page\n")
    driver.find_element_by_id("transport").find_element_by_xpath(".//div[3]/div/button").click()

    return [car_price]