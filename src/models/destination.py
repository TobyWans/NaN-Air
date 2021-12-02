class Destination:
    def __init__(self, destination, country, airport, phone, opening_hour, closing_hour, supervisor):
        self.destination = destination
        self.country = country
        self.airport = airport
        self.phone = phone
        self.opening_hour = opening_hour
        self.closing_hour = closing_hour
        self.supervisor = supervisor

    def __str__(self):
        return f"\nDestination: {self.destination}\nCountry: {self.country}\nAirport: {self.airport}\nPhone: {self.phone}\nOpening hours: {self.opening_hour} -{self.closing_hour}\nSupervisor: {self.supervisor}\n"
