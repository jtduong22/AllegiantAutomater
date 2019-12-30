from AllegiantAutomator import allegiant_automator
from allegiant_config import option

# get initial options file
options_file = 'options.cfg'
options = option()
options.import_config_file(options_file)

# Test and Store results
current_settings = [options.departure_location, options.destination_location, options.departure_date, options.return_date, options.num_of_adults, options.bundle_type, options.is_hotel_booked, options.is_car_booked]
test = allegiant_automator(options, True)

# create file
result_file = open('results.csv', 'w+')

# print out results
p = f"{('FALSE', 'TRUE')[test[0]]:5} {test[1]:6} {test[2]:6} {test[3]}\n "
print(p)
result_file.write(''.join([f"{x};" for x in current_settings + test]) + '\n')

result_file.close()


