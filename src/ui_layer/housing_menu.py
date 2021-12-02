from src.logic_layer.LLAPI import LLAPI
from src.models.housing import Housing

class HousingMenu:
    def __init__(self, llapi):
        self.llapi = llapi
        self.supervisor_options = ["List of housing", "Add housing", "Renting status"]
        self.employee_options = self.llapi.housing_list()
    
    def draw_options(self):
        all_options = []
        all_options.extend(self.employee_options)
        if self.llapi.supervisor_check():
            all_options = self.supervisor_options
            print(f"\tHousing Menu:")
        for index in all_options:
            print(f"\t{all_options.index(index) + 1}. {index}")
        print("\tR. Return\n")
        return self.prompt_input()
        
    def prompt_input(self):
        while True:
            command = input(f"\tEnter your input: ")
            if command == "1":
                housing_list = self.llapi.housing_list()
                for hous in housing_list:
                    print(hous)
            elif command == "2":
                self.add_housing()
            elif command == "3":
                self.renting_status()
            elif command.lower() == "r":
                return
            else:
                print("Invalid option. Try again!")

    def add_housing(self):
        property_number = input("Property_number: ")
        street_name = input("Street_name: ")
        street_number = input("Street_number: ")
        location = input("Location: ")
        size = input("Size: ")
        nr_of_rooms = input("Number of rooms: ")
        type = input("Type: ")
        requires_maintenance = input("Requires maintenance: ")
        hous = Housing(property_number, street_name, street_number, location, size, nr_of_rooms, type, requires_maintenance)
        self.llapi.add_housing(hous)
            
    