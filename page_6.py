from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

# convert from string to int
# avoids float precision issues
def str_dollars_to_cents(price):
    return int(''.join(x for x in price if x.isnumeric()))

# convert from int back to string
def cents_to_dollars(price):
    price = str(price)
    size = len(str(price))
    if size <= 2:
        if size == 1:
            return f'0.{price}0'
        elif size == 2:
            return f'0.{price}'
    else:
        return f'{price[0:size-2]}.{price[size-2:size]}'

# get and compare calculated costs with cost listed on website
def compare_total_price(driver, wait, all_costs):
    print("summing up all costs . . .")
    sum = 0

    # sum up prices
    for price in all_costs:
        sum += str_dollars_to_cents(price)

    print(f"Calculated {cents_to_dollars(sum)}")

    ## compare calculated sum to listed total price on website


    print("Waiting for summary to load. . .")
    # wait for summary to load
    wait.until(ec.presence_of_element_located((By.ID, "summary-wrapper")))

    print("Retrieving listed price on website . . .")
    # get listed price
    summary_row = driver.find_element_by_id("pricing")
    summary_row = summary_row.find_element_by_xpath('.//div/table/tbody[position()=last()-1]/tr/td')
    listed_price = str_dollars_to_cents(summary_row.text)

    print(f"\nCalculated Price was: {cents_to_dollars(sum)}")
    print(f"Listed Price was:     {cents_to_dollars(listed_price)}")
    print(f"The two prices are {('NOT the same', 'identical')[listed_price == sum]}\n")

    return listed_price == sum, cents_to_dollars(sum), cents_to_dollars(listed_price), ('NOT the same', 'identical')[listed_price == sum]
