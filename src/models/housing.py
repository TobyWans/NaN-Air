class Housing:
    def __init__(self, property_number, street_name, street_number, location, size, nr_of_rooms, type, requires_maintenance):
        self.property_number = property_number
        self.street_name = street_name
        self.street_number = street_number
        self.location = location
        self.size = size
        self.nr_of_rooms = nr_of_rooms
        self.type = type
        self.requires_maintenance = requires_maintenance

    def __str__(self):
        return f"{self.property_number:30s}|{self.street_name:20s} {self.street_number:5s}|{self.location:15s}|{self.size:10s}|{self.nr_of_rooms:15s}|{self.type}"