# Test file used learn Selenium
# Tutorial link: https://www.youtube.com/watch?v=FFDDN1C1MEQ

# File opens up google and searches 'Allegiant Airlines'

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

url = 'http://google.com/'


## Load Page ##

driver = webdriver.Firefox()
driver.set_page_load_timeout(10)
driver.get(url)

## Get textbox ##

search_box = driver.find_element_by_name('q')
search_txt = 'allegiant airlines'
search_box.send_keys(search_txt)    # insert text into box
# search_box.submit()               # alternative to code below

## press search button ##
search_button = driver.find_element_by_name('btnK')

# wait until popup box shows up (will throw not visible error otherwise)
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of(driver.find_element_by_class_name('aajZCb')))

# click button and search
search_button.click()







