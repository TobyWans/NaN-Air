class Employee:
    def __init__(self, name, address, email, phone, mobile, location, empid):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone
        self.mobile = mobile
        self.location = location
        self.empid = empid

    def __str__(self):
        return f"ID: {self.empid}\nname: {self.name}\nemail: {self.email}\naddress: {self.address}\nphone: {self.phone}\nmobile: {self.mobile}\nlocation: {self.location}\n"