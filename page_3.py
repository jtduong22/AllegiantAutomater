from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

def parse_bundle_page(driver, wait, bundle_type):
    bundle_type_to_word = {0:"Allegiant Basic", 1:"Allegiant Bonus", 2:"Allegiant Total"}

    bundle_price = '0.00'

    if bundle_type > 0:
        print("Waiting until page loads...")
        wait.until(ec.presence_of_element_located((By.ID, "package")))
        # get bundle price
        print(f"Loaded.  Looking for {bundle_type_to_word[bundle_type]} bundle")

        bundle = None

        c = 0
        for elem in driver.find_element_by_id("package").find_elements_by_xpath(".//fieldset/div/div"):
            if elem.is_displayed() == False:
                continue

            if c == bundle_type:
                bundle = elem.find_element_by_xpath('.//div/div[2]/div[2]')
                print(f"\nFound!\n{bundle.text}")
                break

            c += 1

        if bundle == None:
            raise Exception("Bundle type not found")

        # get bundle price
        bundle_price = bundle.find_element_by_xpath('.//div[2]/i').text

        # select button
        button = bundle.find_element_by_tag_name("button")
        button.click()
        wait.until(ec.staleness_of(bundle))

    print(f"added bundle price is ${bundle_price}")

    # Wait until button is enabled
    # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, "white-overlay")))
    wait.until(ec.element_to_be_clickable((By.CLASS_NAME, "continue")))
    print("Moving onto the next page\n")
    driver.find_element_by_class_name("continue").click()

    return [bundle_price]