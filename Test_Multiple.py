from AllegiantAutomator import allegiant_automator
from allegiant_config import option
from hiddenprints import *

# get and read options file
options_file = 'options.cfg'
options = option()
options.import_config_file(options_file)

# create results file
result_file = open('results.csv', 'w+')
result_file.close()

# counter for keeping track of how many tests left
counter = 1
max_test = 3 * 3 * 2 * 2

# checks 1, 5, and 9 passengers
for num_of_adult in range(1,10,4):
    # checks all 3 types of bundle (basic, plus, and total)
    for bundle in range(3):
        # checks for not booking and booking a hotel
        for hotel_booked in range(2):
            # checks for not booking and booking a car
            for car_booked in range(2):
                print(f"Test {counter} / {max_test}")

                # adjust respective settings
                options.num_of_adults = num_of_adult
                options.bundle_type = bundle
                options.is_hotel_booked = bool(hotel_booked)
                options.is_car_booked = bool(car_booked)

                # put settings into list for easy printing
                current_settings = [options.departure_location, options.destination_location, options.departure_date,
                                    options.return_date, options.num_of_adults, options.bundle_type,
                                    options.is_hotel_booked, options.is_car_booked]

                print(current_settings)

                test = []
                # Test and Store results
                with HiddenPrints():            # hide terminal output
                    test = allegiant_automator(options)

                # print results
                p = f"{('FALSE', 'TRUE')[test[0]]:5} {test[1]:6} {test[2]:6} {test[3]}\n "
                print(p)

                # write results to file
                result_file = open("results.csv",'a')
                result_file.write(''.join([f"{x};" for x in current_settings + test]) + '\n')
                result_file.close()

                counter += 1

