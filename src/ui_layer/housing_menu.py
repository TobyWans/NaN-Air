from src.logic_layer.LLAPI import LLAPI
from src.models.housing import Housing

class HousingMenu:
    def __init__(self, llapi):
        self.llapi = llapi
        self.supervisor_options = ["List of housing", "Add housing", "Renting status"]
        self.employee_options = self.housing_list()
    
    def draw_options(self):
        self.llapi.clear_console()
        all_options = []
        all_options.extend(self.supervisor_options)
        for index in all_options:
            print(f"\t{all_options.index(index) + 1}. {index}")
        print("\tQ. Return\n")
        return self.prompt_input()

    def prompt_input(self):
        while True:
            command = input("Enter your input: ")
            if command == "1":
                self.housing_list()
            if command == "2":
                self.add_housing()
            elif command == "r":
                self.renting_status()
            else:
                print("Invalid option. Try again!")
            print(self.options)

    def housing_list():
        pass

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

    def change_housing():
        pass

    def renting_status():
        pass
            
    