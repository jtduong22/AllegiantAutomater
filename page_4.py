from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

def parse_hotel_page(driver, wait, is_booked_hotel):
    hotel_price = '0.00'

    if is_booked_hotel:
        print("Waiting for page to load. . .")
        wait.until(ec.presence_of_element_located((By.ID, "hotelchooser")))

        print("Page loaded. Retrieving price of first hotel")
        hotel_chooser = driver.find_element_by_id("hotelchooser")
        hotel_listing = hotel_chooser.find_element_by_xpath('.//div[4]/div[2]/div[1]/div/div[2]/div[2]/div/div/div[2]')

        print("Price found. Selecting hotel")
        hotel_price = hotel_listing.find_element_by_xpath('.//strong').text
        hotel_listing.find_element_by_tag_name("button").click()

        print("Looking for book button")
        book_button = hotel_chooser.find_element_by_xpath('.//div[4]/div[2]/div[1]/div/div[3]/div/div[1]/div/div/ul/li[1]/div[1]/div[2]/div/div[2]/div/div[2]/button')
        book_button.click()


    print(f"added hotel price is {hotel_price}")

    # Wait until button is enabled
    wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, "white-overlay")))
    wait.until(ec.element_to_be_clickable((By.CLASS_NAME, "continue")))
    print("Moving onto the next page\n")
    driver.find_element_by_class_name("continue").click()

    return [hotel_price]