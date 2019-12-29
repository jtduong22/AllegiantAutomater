from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

def parse_car_page(driver, wait):
    car_price = '0.00'

    print(f"added car price is ${car_price}")

    # Wait until button is enabled
    # wait.until(ec.presence_of_element_located((By.ID, "vehicles")))
    wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, "white-overlay")))
    wait.until(ec.element_to_be_clickable((By.CLASS_NAME, "continue")))
    print("Moving onto the next page\n")
    driver.find_element_by_class_name("continue").click()

    return [car_price]