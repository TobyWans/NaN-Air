from src.logic_layer.LLAPI import LLAPI
from src.models.housing import Housing

class HousingMenu:
    def __init__(self, llapi:LLAPI):
        self.llapi = llapi
        self.supervisor_options = ["List of housing", "Add housing","Change housing", "Renting status"]
        self.employee_options = self.llapi.housing_list()
    
    def draw_options(self):
        self.llapi.clear_console()
        all_options = []
        all_options.extend(self.employee_options)
        if self.llapi.supervisor_check():
            all_options = self.supervisor_options
            print(f"\tHousing Menu:")
            for line in all_options:
                print(f"\t{all_options.index(line) + 1}. {line}")
        else:
            print(f"\tHousing List:")
            for line in all_options:
                print(f"{line}")
        print("\tR. Return\n")

        
    def prompt_input(self):
        while True:
            self.draw_options()
            command = input(f"\tEnter your input: ")
            if command == "1":
                    housing_list = self.llapi.housing_list()
                    for hous in housing_list:
                        print(hous)
                    back = input("Enter to continue")
                    self.llapi.clear_console()
            elif command == "2":
                    self.add_housing()
            elif command == "3":
                    search_by_housing_id = "Invalid input!" #it can be constant
                    while search_by_housing_id == "Invalid input!": 
                        id_input = input("Please enter the property ID: ")
                        search_by_housing_id = self.llapi.search_by_housing_id(id_input)
                        print(search_by_housing_id)
                    wait = input("Press enter to contine") #it can be constant
                #Bæta quit
            elif command == "4":
                free_to_rent, booked = self.llapi.rental_status()
                print (f"\tFree to rent: ")
                for line in free_to_rent:
                    print(f"{line}")
                print("\n\tBooked:")
                for line in booked:
                    print(f"{line}")
                wait = input("Press enter to contine") #maybe it can be constant
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
            
    