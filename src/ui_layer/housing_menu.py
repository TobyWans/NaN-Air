from src.logic_layer.LLAPI import LLAPI
from src.models.housing import Housing
import time

ENTER = "\n\tPress enter to continue"
RETURN = "\t\tR. Return"
INVALID = "\n\tInvalid input. Try again!\n"
SPLASH_SCREEN = """_____   __                   ____________        
___  | / /_____ _______      ___    |__(_)_______
__   |/ /_  __ `/_  __ \     __  /| |_  /__  ___/
_  /|  / / /_/ /_  / / /     _  ___ |  / _  /    
/_/ |_/  \__,_/ /_/ /_/      /_/  |_/_/  /_/     
                                                 """


class HousingMenu:
    def __init__(self, llapi:LLAPI):
        self.llapi = llapi
        self.supervisor_options = ["Add housing","Check/Change housing"]
        self.employee_options = ["List of housing","Search by Id", "Renting status"]
    
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
        print(SPLASH_SCREEN)
        all_options = []
        all_options.extend(self.employee_options)
        if self.llapi.supervisor_check():
            all_options.extend(self.supervisor_options)
        self.main_header("Housing Menu")
        print()
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
                search = self.search_by_id()
                if search != None:
                    input(ENTER)
            elif command == "3":
                self.rental_status()
            elif command == "4" and self.llapi.supervisor_check():
                self.add_housing()
            elif command == "5" and self.llapi.supervisor_check():
                self.change_housing()
            elif command.lower() == "r":
                return
            else:
                print(INVALID)
                time.sleep(1)

    def sort_by_location(self): 
        self.llapi.clear_console()
        print(SPLASH_SCREEN)
        self.main_header("List of housing", 133)
        print("-".center(133, '-'))
        housing_list = self.llapi.housing_list() # the list of all properties/ not sorted
        location_list = self.llapi.location_list() # The list of all location where company has property
        if self.llapi.supervisor_check():
            for location in location_list: 
                print(location.center(133, ' '))
                self.header(f"{'Property ID':^13}|{'Street name and number':^30}|{'Location':^20}|{'m2':^13}|{'Rooms':^30}|{'Type':^20}", 133)
                for row in housing_list:
                    if location in row.values():
                        hous = Housing(**row)
                        print(f"{hous}")
                        print()
                print("-".center(133, '-'))
        if not self.llapi.supervisor_check():
            user_location = self.llapi.location_check()
            for location in location_list:
                if user_location == location:
                    print(location.center(133, ' '))
                    self.header(f"{'Property ID':^13}|{'Street name and number':^30}|{'Location':^20}|{'m2':^13}|{'Rooms':^30}|{'Type':^20}", 133)
                    for row in housing_list:
                        if location in row.values():
                            hous = Housing(**row)
                            print(f"{hous}")
                            print()
        input(ENTER)
        self.llapi.clear_console()
            
    def search_by_id(self): #Searching for property with given Id number
        self.llapi.clear_console()
        print(SPLASH_SCREEN)
        print("Search for property by ID number".center(48, '-'))
        the_id = None
        running = True
        id_input = input("\nEnter property ID: ")
        self.llapi.clear_console()
        print(SPLASH_SCREEN)
        print("Search for property by ID number".center(48, '-'))
        if id_input.lower() == 'r':
            running = False
        print()
        while running:
            search_by_id = self.llapi.search_by_housing_id(id_input)
            if search_by_id == None:
                print("\nSorry, there are no properties with that ID\n".center(48))
                id_input = input("Search for another ID or type r to return: ")
                self.llapi.clear_console()
                print(SPLASH_SCREEN)
                print("Search for property by ID number".center(48, '-'))
                if id_input.lower() == 'r':
                    running = False
                    return None
            else:
                print(f"{search_by_id}")
                the_id = id_input
                running = False
                return the_id #Returns id_number

    def rental_status(self): #Prints out locations segregated with rental status : free to book or booked
        self.llapi.clear_console()
        print(SPLASH_SCREEN)
        self.main_header("Renting status", 133)
        print("-".center(133, '-'))
        if not self.llapi.supervisor_check():
            user_location = self.llapi.location_check() 
            free_to_rent, booked = self.llapi.rental_status_by_location(user_location) #if not supervisor prints only housing which are at the same location as employee
        else:
            free_to_rent, booked = self.llapi.rental_status()
        print("Free to rent".center(133, ' '))
        if len(free_to_rent) != 0:
            self.header(f"{'Property ID':^13}|{'Street name and number':^30}|{'Location':^20}|{'m2':^13}|{'Rooms':^30}|{'Type':^20}",133)
            for line in free_to_rent:
                print(f"{line}")
                print()
            print("-".center(133, '-'))
        else:
            print("Nothing to display".center(133, ' '))
            print()
        print("Booked".center(133, ' '))
        if len(booked) != 0:
            self.header(f"{'Property ID':^13}|{'Street name and number':^30}|{'Location':^20}|{'m2':^13}|{'Rooms':^30}|{'Type':^20}",133)
            for line in free_to_rent:
                print(f"{line}")
                print()
            print("-".center(133, '-'))
        else:
            print("Nothing to display".center(133, ' '))
            print()
        input(ENTER)

    def add_housing(self): #supervisor can add property in location where he works 
        self.llapi.clear_console()
        print(SPLASH_SCREEN)
        print("Add property".center(48, '-'))
        user_id = self.llapi.curent_user
        supervisor = self.llapi.employee_name(user_id)
        property_number = input("Property_number: ")
        search_by_property_num = self.llapi.search_by_housing_id(str(property_number))
        while search_by_property_num != None:
            print('Entered ID already exists. Try another number!')
            property_number = input("Property_number: ")
            search_by_property_num = self.llapi.search_by_housing_id(property_number)
        street_name = None
        while street_name == None:
            street_name = input("Street_name: ")
            for letter in street_name:
                if letter.isdigit():
                    print("Input only letters!")
                    street_name = None
                    break
        street_number = None
        while street_number == None:
            try:
                street_number = int(input("Street_number: "))
            except ValueError:
                print(INVALID)
                street_number = None
        city = self.llapi.location_check()
        location = city
        size_in_m2 = None
        while size_in_m2 == None:
            try:
                size_in_m2 = int(input("Size in m2: "))
            except ValueError:
                print(INVALID)
                size_in_m2 = None
        nr_of_rooms = None
        while nr_of_rooms == None:
            try:
                nr_of_rooms = int(input("Number of rooms: "))
            except ValueError:
                print(INVALID)
                nr_of_rooms = None
        type = None
        while type == None:
            type = input("Type: ")
            for letter in type:
                if letter.isdigit():
                    print("Input only letters!")
                    type = None
                    break
        requires_maintenance = input("Requires maintenance(If nothing to add press enter): ")
        rental_status = input("Please input rental status(free to rent/booked/not applicable): ")
        while rental_status.lower() != "free to rent" and rental_status.lower() != "booked" and rental_status.lower() != "not applicable":
            print(INVALID)
            rental_status = input("Please input rental status(free to rent/booked/not applicable):")
        confirm = ""
        while confirm != "y" and confirm != "n":
            confirm = input("Confirm? (y/n): ")
            if confirm.lower() == "y":
                hous = Housing(supervisor, property_number, street_name, street_number, location, size_in_m2, nr_of_rooms, type, requires_maintenance.lower(), rental_status.lower())
                self.llapi.add_housing(hous)
                print("Housing successfully created")
                time.sleep(1.8)
            elif confirm.lower() == "n":
                return
            else:
                print(INVALID)

    def change_housing(self): #Function first ask for ID of property, checks if property with given ID exists, if yes than supervisor can update information about location
        self.llapi.clear_console()
        print(SPLASH_SCREEN)
        print("Search for property by ID number".center(48, '-'))
        id_number = self.search_by_id()
        if id_number != None:
            confirm = ""
            while confirm != "y" and confirm != "n":
                confirm = input(f"\nDo you want to change information for the property displayed above?\n\t\tID number: {id_number}(y/n)?  ")
                if confirm.lower() == "y":
                    user_id = self.llapi.curent_user
                    supervisor = self.llapi.employee_name(user_id)
                    property_number = id_number
                    street_name = None
                    while street_name == None:
                        street_name = input("Street_name: ")
                        for letter in street_name:
                            if letter.isdigit():
                                print("Input only letters!")
                                street_name = None
                                break
                    street_number = None
                    while street_number == None:
                        try:
                            street_number = int(input("Street_number: "))
                        except ValueError:
                            print(INVALID)
                            street_number = None
                    city = self.llapi.location_check()
                    location = city
                    size_in_m2 = None
                    while size_in_m2 == None:
                        try:
                            size_in_m2 = int(input("Size in m2: "))
                        except ValueError:
                            print(INVALID)
                            size_in_m2 = None
                    nr_of_rooms = None
                    while nr_of_rooms == None:
                        try:
                            nr_of_rooms = int(input("Number of rooms: "))
                        except ValueError:
                            print(INVALID)
                            nr_of_rooms = None
                    type = None
                    while type == None:
                        type = input("Type: ")
                        for letter in type:
                            if letter.isdigit():
                                print("Input only letters!")
                                type = None
                                break                    
                    requires_maintenance = input("Requires maintenance(If nothing to add press enter): ")
                    rental_status = input("Please input rental status(free to rent/booked/not applicable): ")
                    while rental_status.lower() != "free to rent" and rental_status.lower() != "booked" and rental_status.lower() != "not applicable":
                        print(INVALID)
                        rental_status = input("Please input rental status(free to rent/booked/not applicable):")
                    confirm = ""
                    while confirm != "y" and confirm != "n":
                        confirm = input("Confirm? (y/n): ")
                        if confirm.lower() == "y":
                            changed_hous = Housing(supervisor, property_number, street_name, street_number, location, size_in_m2, nr_of_rooms, type, requires_maintenance.lower(), rental_status.lower())
                            self.llapi.change_housing(id_number, changed_hous)
                            print("Housing information successfully updated")
                            time.sleep(1.8)
                        elif confirm.lower() == "n":
                            return
                        else:
                            print(INVALID)            
                elif confirm.lower() == "n":
                    return
                else:
                    print(INVALID)