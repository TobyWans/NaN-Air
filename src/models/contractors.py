class contractors:
    def __init__(self, contractor, name, profession, phone, opening_hours, location, rating):
        self.contractor = contractor
        self.name = name
        self.profession = profession
        self.phone = phone
        self.opening_hours = opening_hours
        self.location = location
        self.rating = rating

    def __str__(self):      # Gets called whenever the user wants to see a contractor's full information
        return f"{'Contractor:':<25} {self.contractor}\n{'Phone:':<25} {self.phone}\n{'Name:':<25} {self.name}\n{'Opening Hours:':<25} {self.opening_hours}\n{'Location:':<25} {self.location}\n{'Profession:':<25} {self.profession}\n{'Rating:':<25} {self.rating}/10\n"

    def display(self):      # Gets called in the main contractor's menu as a thumbnail or summary of a contractor
        return f"{self.contractor:<25} - {self.profession:<20} - {self.location}"