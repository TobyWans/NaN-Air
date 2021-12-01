class Employee:
    def __init__(self, name, address, email, phone, mobile, location):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone
        self.mobile = mobile
        self.location = location

    def __str__(self):
        return f"name: {self.name}, email: {self.email},address {self.address} phone: {self.phone}, mobile {self.mobile}, location{self.location}"