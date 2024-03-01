class Truck:
    def __init__(self, average_speed, miles, current_location, time_of_departure, packages):
        self.average_speed = average_speed
        self.miles = miles
        self.current_location = current_location
        self.time_of_departure = time_of_departure
        self.packages = packages

    def __str__(self):
        return "%s,%s,%s,%s,%s,%s" % (self.average_speed, self.miles, self.current_location, self.time_of_departure, self.packages)