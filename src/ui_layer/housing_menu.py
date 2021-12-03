from src.logic_layer.LLAPI import LLAPI
from src.models.housing import Housing

class HousingMenu:
    def __init__(self, llapi:LLAPI):
        self.llapi = llapi
        self.supervisor_options = ["List of housing", "Add housing","Change housing", "Renting status"]
        self.employee_options = []
    
    def draw_options(self):
        self.llapi.clear_console()
        supervisor_options = self.supervisor_options
        if self.llapi.supervisor_check():
            print(f"\tHousing Menu:")
            for line in supervisor_options:
                print(f"\t{supervisor_options.index(line) + 1}. {line}")         
        else:
            print(f"\tHousing List:")
            self.sort_by_location()
        print("\n\tR. Return\n") 

    def prompt_input(self):
        while True:
            self.draw_options()
            command = input(f"\tEnter your input: ")
            if command == "1":
                self.sort_by_location()
            elif command == "2":
                self.add_housing()
            elif command == "3":
                self.search_by_id()
            elif command == "4":
                self.rental_status()
            elif command.lower() == "r":
                return
            else:
                print("Invalid option. Try again!")

    def add_housing(self):
        supervisor = input("Enter your full name:") # Should probably automaticly adding the name of supervisor which is loged in 
        property_number = input("Property_number: ")
        street_name = input("Street_name: ")
        street_number = input("Street_number: ")
        location = input("Location: ")
        size = input("Size: ")
        nr_of_rooms = input("Number of rooms: ")
        type = input("Type: ")
        requires_maintenance = input("Requires maintenance: ")
        rental_status = input("Please enter rental status(free to rent/booked): ")
        hous = Housing(supervisor, property_number, street_name, street_number, location, size, nr_of_rooms, type, requires_maintenance, rental_status)
        self.llapi.add_housing(hous)
    
    def sort_by_location(self):
        hous_list = []
        housing_list = self.llapi.housing_list()
        location_list = self.llapi.location_list()
        hous_list.extend(housing_list)
        for location in location_list:
            print(f"\n\t***{location}***")
            for row in hous_list:
                if location in row.values():
                    hous = Housing(**row)
                    print(f"{hous}")
        if self.llapi.supervisor_check():
            wait = input("Press enter to contine")

    def rental_status(self):
        free_to_rent, booked = self.llapi.get_rental_status()
        print (f"\tFree to rent: ")
        for line in free_to_rent:
            print(f"{line}")
        print("\n\tBooked:")
        for line in booked:
            print(f"{line}")
        wait = input("Press enter to contine") #maybe it can be constant

    def search_by_id(self):
        search_by_housing_id = "Invalid input!" #it can be constant
        while search_by_housing_id == "Invalid input!": 
            id_input = input("Please enter the property ID: ")
            search_by_housing_id = self.llapi.search_by_housing_id(id_input)
            print(search_by_housing_id)
        wait = input("Press enter to contine") #it can be constant
    #Bæta quit
