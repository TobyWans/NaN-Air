from src.logic_layer.LLAPI import LLAPI
from src.models.housing import Housing

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
    
    def draw_options(self):
        self.llapi.clear_console()
        print(self.splash_screen)
        all_options = []
        all_options.extend(self.employee_options)
        if self.llapi.supervisor_check():
            all_options.extend(self.supervisor_options)
        print("Housing Menu:".center(48, '-'))
        for index in all_options:
            print(f"\t\t{all_options.index(index) + 1}. {index}")
        print("\t\tR. Return\n")
        
    def prompt_input(self):
        while True:
            self.draw_options()
            command = input(f"\tEnter your input: ")
            if command == "1":
                self.sort_by_location()
                if self.llapi.supervisor_check():
                    self.id_menu_option()
            elif command == "2":
                self.search_by_id()
            elif command == "3":
                self.rental_status()
            elif command == "4":
                self.add_housing()
            elif command == "5":
                self.search_by_id()
            elif command.lower() == "r":
                return
            else:
                print("Invalid option. Try again!")

    def sort_by_location(self):
        housing_list = self.llapi.housing_list()
        location_list = self.llapi.location_list()
        if self.llapi.supervisor_check():
            for location in location_list:
                print(f"\n\t***{location}***")
                for row in housing_list:
                    if location in row.values():
                        hous = Housing(**row)
                        print(f"{hous}")
        if not self.llapi.supervisor_check():
            user_location = self.llapi.location_check()
            for location in location_list:
                if user_location == location:
                    print(f"\n\t***{location}***")
                    for row in housing_list:
                        if location in row.values():
                            hous = Housing(**row)
                            print(f"{hous}")
            input("\n\tPress enter to continue\n")
            self.llapi.clear_console()

    def id_menu_option(self):
        print("\n\tS. Search by Id")
        print("\tR. Return")
        command = (input(f"\n\tEnter your input: "))
        if command.lower() == "s":
            self.llapi.clear_console()
            self.search_by_id()
            
    def search_by_id(self):
        search_by_housing_id = "Invalid input!" #it can be constant
        while search_by_housing_id == "Invalid input!": 
            id_input = input("Please enter the property ID: ")
            search_by_housing_id = self.llapi.search_by_housing_id(id_input)
            print(search_by_housing_id)
        wait = input("Press enter to contine") #it can be constant
        #Bæta quit

    def rental_status(self):
        user_location = self.llapi.location_check()
        free_to_rent, booked = self.llapi.get_rental_status(user_location)
        print (f"\n\t***Free to rent***")
        for line in free_to_rent:
            print(f"{line}")
        print("\n\t***Booked***")
        for line in booked:
            print(f"{line}")
        wait = input("Press enter to contine") #maybe it can be constant

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

    def change_housing(self):
        pass
    



