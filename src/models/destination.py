class Destination:
    def __init__(self, destination_ID, country, airport, phone, opening_hour, closing_hour, supervisor):
        self.destination = destination_ID
        self.airport = airport
        self.country = country
        self.phone = phone
        self.opening_hour = opening_hour
        self.closing_hour = closing_hour
        self.supervisor = supervisor

    def __str__(self):
        return f"country: {self.country}, airport: {self.airport}, phone: {self.phone}, opening hours: {self.opening_hour} - {self.closing_hour}, supervisor: {self.supervisor}"

