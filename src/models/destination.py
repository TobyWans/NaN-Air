class Destination:
    def __init__(self, airport, phone, hours, supervisor):
        self.airport = airport
        self.phone = phone
        self.hours = hours
        self.supervisor = supervisor

    def __str__(self):
        return f"airport: {self.airport}, phone: {self.phone}, hours: {self.hours}, supervisor: {self.supervisor}"