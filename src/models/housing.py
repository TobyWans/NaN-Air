class Housing:
    def __init__(self, supervisor, property_number, street_name, street_number, location, size, nr_of_rooms, type, requires_maintenance, rental_status):
        self.supervisor = supervisor
        self.property_number = property_number
        self.street_name = street_name
        self.street_number = street_number
        self.location = location
        self.size = size
        self.nr_of_rooms = nr_of_rooms
        self.type = type
        self.requires_maintenance = requires_maintenance
        self.rental_status = rental_status

    def __str__(self):
        return f"{self.property_number:10} {self.street_name:20s} {self.street_number:3s}, {self.location:15s}|{self.size:10s}|{self.nr_of_rooms:15s}|{self.type}"

    def only_housing_id(self):
        return f"{self.property_number}"

class Particular_real_estate:
    def __init__(self, supervisor, property_number, street_name, street_number, location, size, nr_of_rooms, type, requires_maintenance, rental_status):
        self.supervisor = supervisor
        self.property_number = property_number
        self.street_name = street_name
        self.street_number = street_number
        self.location = location
        self.size = size
        self.nr_of_rooms = nr_of_rooms
        self.type = type
        self.requires_maintenance = requires_maintenance
        self.rental_status = rental_status

    def __str__(self):
        return f"\nAdress: {self.street_name} {self.street_number}, {self.location:25s} \nSize: {self.size} \nNumber of rooms: {self.nr_of_rooms} \nType: {self.type} \nRequires maintenance: {self.requires_maintenance}"