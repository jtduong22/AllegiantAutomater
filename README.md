# AllegiantAutomator
Code Challenge to automate AllegiantAir.com
This project navigates from the front page of [AllegiantAir.com](allegiantair.com) to the travellers page. It compares the summed price of all the selected flights, hotels, and/or vehicles and compares to the listed price in the summary.

Currently allows:
* adjustment of departure and destination location
* adjustment of departure and return dates
* adjustment of number of adults on the trip 

Does not allow as of currently:
* non-round trips
* adding any children
* selecting a hotel
* selecting a vehicle

## Getting Started

### Pre-requisites
* Python 3.6
  * Selenium 3.141.0
    * can be installed via 
```pip3 install selenium``` in the terminal
  * ConfigParser
     * can be installed via 
    ```pip3 install ConfigParser``` in the terminal
* Firefox Geckodriver
  * download the latest version [here](https://github.com/mozilla/geckodriver/releases) and place in the ```/usr/local/bin/``` directory
* Firefox

### Running
* Adjust any settings in AllegiantAutomator.py as desired
* run the following code
```
cd (directory of code)
python3 AllegiantAutomator.py
```
* The results will once the travelers page is reached

## Issues
* Script will every now and then stop and throw an error on the initial credit card pop up
* Sometimes the script will hang for about 10 seconds on the Hotel and/or Vehicle page
* Script currently will stop immediately on the flights page if in mobile page. If this occurs, zoom out
