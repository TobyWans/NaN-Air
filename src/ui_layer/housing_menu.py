from src.logic_layer.LLAPI import LLAPI
from src.models.housing import Housing
import time

ENTER = "\n\tPress enter to continue"
RETURN = "\t\tR. Return"
INVALID = "Invalid option. Try again!"

class HousingMenu:
    def __init__(self, llapi:LLAPI):
        self.llapi = llapi
        self.supervisor_options = ["Add housing","Check/Change housing"]
        self.employee_options = ["List of housing","Search by Id", "Renting status"]
        self.splash_screen = """_____   __                   ____________        
___  | / /_____ _______      ___    |__(_)_______
__   |/ /_  __ `/_  __ \     __  /| |_  /__  ___/
_  /|  / / /_/ /_  / / /     _  ___ |  / _  /    
/_/ |_/  \__,_/ /_/ /_/      /_/  |_/_/  /_/     
                                                 """
    
    def main_header(self, text, size=48):
        print("=".center(size, '='))
        print(f"{text}".center(size, ' '))
        print("=".center(size, '='))
    
    def header(self, text, size):
        print("-".center(size, '-'))
        print (f"{text}".center(size, ' '))
        print("-".center(size, '-'))
    
    def draw_options(self):
        self.llapi.clear_console()
        print(self.splash_screen)
        all_options = []
        all_options.extend(self.employee_options)
        if self.llapi.supervisor_check():
            all_options.extend(self.supervisor_options)
        self.main_header("Housing Menu")
        for index in all_options:
            print(f"\t\t{all_options.index(index) + 1}. {index}")
        print(RETURN)
        
    def prompt_input(self):
        while True:
            self.draw_options()
            command = input(f"\n\tEnter your input: ")
            if command == "1":
                self.sort_by_location()
            elif command == "2":
                self.search_by_id()
            elif command == "3":
                self.rental_status()
            elif command == "4":
                self.add_housing()
            elif command == "5":
                self.change_housing()
            elif command.lower() == "r":
                return
            else:
                print(INVALID)

    def sort_by_location(self):
        housing_list = self.llapi.housing_list()
        location_list = self.llapi.location_list()
        self.llapi.clear_console()
        if self.llapi.supervisor_check():
            for location in location_list:
                self.header(location, 90)
                for row in housing_list:
                    if location in row.values():
                        hous = Housing(**row)
                        print(f"{hous}")
        if not self.llapi.supervisor_check():
            user_location = self.llapi.location_check()
            for location in location_list:
                if user_location == location:
                    self.header(location, 90)
                    for row in housing_list:
                        if location in row.values():
                            hous = Housing(**row)
                            print(f"{hous}")
        input(ENTER)
        self.llapi.clear_console()
            
    def search_by_id(self):
        running = True
        id_input = input("Please enter the ID of property or type r to return: ")
        if id_input.lower() == 'r':
            running = False
        while running:
            self.llapi.clear_console()
            self.splash_screen
            print("Search for property by ID number".center(48, '-'))
            search_by_id = self.llapi.search_by_housing_id(id_input)
            if search_by_id == None:
                print("\nSorry, there are no properties with that ID\n".center(48))
                id_input = input("Please try another ID or type r to return: ")
                if id_input.lower() == 'r':
                    running = False
                print()
            else:
                print(f"\n{search_by_id}")
                id_input = input("\nEnter another ID to search or type r to return: ")
                self.llapi.clear_console()
                if id_input.lower() == 'r':
                    running = False

    def rental_status(self):
        if not self.llapi.supervisor_check():
            user_location = self.llapi.location_check()
            free_to_rent, booked = self.llapi.rental_status_by_location(user_location)
        else:
            free_to_rent, booked = self.llapi.rental_status()
            self.main_header("Free to rent",155)
            for line in free_to_rent:
                print(f"{line}")
                print (f"-".center(155,'-'))
            self.main_header("Booked",155)
            for line in booked:
                print(f"{line}")
                print (f"-".center(155,'-'))
        input(ENTER)

    def add_housing(self):
        user_id = self.llapi.curent_user
        supervisor = self.llapi.employee_name(user_id)
        property_number = input("Property_number: ")
        street_name = input("Street_name: ")
        street_number = input("Street_number: ")
        city = self.llapi.location_check()
        location = city
        size = input("Size: ")
        nr_of_rooms = input("Number of rooms: ")
        type = input("Type: ")
        requires_maintenance = input("Requires maintenance: ")
        rental_status = input("Please enter rental status(free to rent/booked): ")
        hous = Housing(supervisor, property_number, street_name, street_number, location, size, nr_of_rooms, type, requires_maintenance, rental_status)
        self.llapi.add_housing(hous)

    def change_housing(self):
        id_number = input("Input ID number: ")
        print("\nWhat would you want to change?\n\n1. Street name\n2. Street number\n3. Size\n4. Numbers of rooms\n5. Type\n6. Requires maintenance\n7. Rental status")
        change = input("\nEnter a number: ")
        change = int(change)
        if change == 1:
            fieldname = "street_name"
            parametr = input("Street_name: ")
        elif change == 2:
            fieldname = "street_number"
            parametr = input("Street_number: ")
        elif change == 3:
            fieldname = "location"
            parametr = input("size: ")
        elif change == 4:
            fieldname = "nr_of_rooms"
            parametr = input("Numbers of rooms: ")
        elif change == 5:
            fieldname = "type"
            parametr = input("Type: ")
        elif change == 6:
            fieldname = "requires_maintenance"
            parametr = input("Requires maintenance: ")
        elif change == 7:
            fieldname = "rental_status"
            parametr = input("Rental status: ")
        else:
            print(INVALID)

        self.llapi.change_housing(id_number, fieldname, parametr)
