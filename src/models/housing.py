class Housing:
    def __init__(self, supervisor, property_number, street_name, street_number, location, size_in_m2, nr_of_rooms, type, requires_maintenance, rental_status):
        self.supervisor = supervisor
        self.property_number = property_number
        self.street_name = street_name
        self.street_number = street_number
        self.location = location
        self.size_in_m2 = size_in_m2
        self.nr_of_rooms = nr_of_rooms
        self.type = type
        self.requires_maintenance = requires_maintenance
        self.rental_status = rental_status

    def __str__(self):
        return f"{self.property_number:^13}|{self.street_name:^27}{self.street_number:<3}|{self.location:^20}|{self.size_in_m2:^13}|{self.nr_of_rooms:^30}|{self.type:^20}"     
    def only_housing_id(self):
        return f"{self.property_number}"

class Particular_real_estate:
    def __init__(self, supervisor, property_number, street_name, street_number, location, size_in_m2, nr_of_rooms, type, requires_maintenance, rental_status):
        self.supervisor = supervisor
        self.property_number = property_number
        self.street_name = street_name
        self.street_number = street_number
        self.location = location
        self.size_in_m2 = size_in_m2
        self.nr_of_rooms = nr_of_rooms
        self.type = type
        self.requires_maintenance = requires_maintenance
        self.rental_status = rental_status

    def __str__(self):
        return f"\n\t Property number: {self.property_number}\n\nSupervisor: {self.supervisor} \nAdress: {self.street_name} {self.street_number}, {self.location} \nSize: {self.size_in_m2}m2 \nNumber of rooms: {self.nr_of_rooms} \nType: {self.type} \nRequires maintenance: {self.requires_maintenance}\nRental status: {self.rental_status}"