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
        return f"Property_number: {self.property_number}, Adress: {self.street_name} {self.street_number}, {self.location}, Size: {self.size}, Number of rooms: {self.nr_of_rooms}, Type of house: {self.type}, Requires maintenance: {self.requires_maintenance}" 