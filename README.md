# AllegiantAutomator
Code Challenge to automate AllegiantAir.com
This project navigates from the front page of [AllegiantAir.com](allegiantair.com) to the travellers page. It compares the summed price of all the selected flights, hotels, and/or vehicles and compares to the listed price in the summary. It then prints the results in a csv file for easy viewing in any spreadsheet program.

Currently allows:
* adjustment of departure and destination location
* adjustment of departure and return dates
* adjustment of number of adults on the trip
* select bundle type
* selecting a hotel
* selecting a vehicle

Does not allow as of currently:
* non-round trips
* adding any children

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
* Adjust any settings in options.cfg as desired
* run the following code to run a single test
```
cd (directory of code)
python3 Test_Single.py
```
* to run multiple tests, call ```Test_Multiple.py``` instead
* The results will show in the terminal  once the travelers page is reached

## Issues
* Script currently will stop immediately on the flights page if in mobile page. If this occurs, zoom out
* Options does not yet have error checking so it's possible to read in invalid options
* Script will every now and then stop and throw an error on the initial credit card pop up