class Employee:
    def __init__(self, name, address, email, phone, mobile):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone
        self.mobile = mobile

    def __str__(self):
        return f"name: {self.name}, email: {self.email},address {self.address} phone: {self.phone}, mobile {self.mobile}"