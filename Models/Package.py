class Package:
    def __init__(self, package_id, delivery_street, delivery_city, delivery_state, delivery_zip, delivery_deadline, package_weight, delivery_notes, delivery_status, time_of_departure, time_of_delivery):
        self.package_id = package_id
        self.delivery_street = delivery_street
        self.delivery_city = delivery_city
        self.delivery_state = delivery_state
        self.delivery_zip = delivery_zip
        self.delivery_deadline = delivery_deadline
        self.package_weight = package_weight
        self.delivery_notes = delivery_notes
        self.delivery_status = delivery_status
        self.time_of_departure = time_of_departure
        self.time_of_delivery = time_of_delivery