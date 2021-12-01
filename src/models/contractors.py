class contractors:
    def __init__(self, contractor, name, profession, phone, opening_hours, location, rating):
        self.contractor = contractor
        self.name = name
        self.profession = profession
        self.phone = phone
        self.opening_hours = opening_hours # string format
        self.location = location
        self.rating = rating

    def show_all_info(self):
        return f"Contractor: {self.contractor}\nPhone: {self.phone}\nName: {self.name}\nOpening Hours: {self.opening_hours}\nLocation: {self.location}\nProfession: {self.profession}\nRating: {self.rating}\n"

    def  __str__(self):
        return f"{self.contractor} | {self.profession}"