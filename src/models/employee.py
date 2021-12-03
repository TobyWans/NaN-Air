class Employee:
    def __init__(self, name, address, email, phone, mobile, location, id):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone
        self.mobile = mobile
        self.location = location
        self.id = id

    def __str__(self):
        return f"ID: {self.id}\nname: {self.name}\nemail: {self.email}\naddress: {self.address}\nphone: {self.phone}\nmobile: {self.mobile}\nlocation: {self.location}"