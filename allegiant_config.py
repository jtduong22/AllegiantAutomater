import configparser

class option:
    def __init__(self):
        self.departure_location = ""
        self.destination_location = ""
        self.departure_date = []
        self.return_date = []
        self.num_of_adults = 1
        self.bundle_type = 1
        self.is_hotel_booked = False
        self.is_car_booked = False

    def import_config_file(self, filename):
        config = configparser.ConfigParser()
        config.read(filename)

        # import settings from file
        self.departure_location = config['Intro']['departure_location']
        self.destination_location = config['Intro']['destination_location']
        self.departure_date = [int(x) for x in config['Intro']['departure_date'].split(',')]
        self.return_date = [int(x) for x in config['Intro']['return_date'].split(',')]
        self.num_of_adults = int(config['Intro']['num_of_adults'])
        self.bundle_type = int(config["Bundle"]['bundle_type'])
        self.is_hotel_booked = config.getboolean('Hotel','is_hotel_booked')
        self.is_car_booked = config.getboolean('Car','is_car_booked')

    def print(self):
        print(self.departure_location)
        print(self.destination_location)
        print(self.departure_date)
        print(self.return_date)
        print(self.num_of_adults)
        print(self.bundle_type)
        print(self.is_hotel_booked)
        print(self.is_car_booked)
