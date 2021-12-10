from src.logic_layer.LLAPI import LLAPI
from src.models.contractors import contractors
import time

from src.ui_layer.housing_menu import INVALID

class ContractorMenu:
    def __init__(self, llapi: LLAPI):
        self.llapi = llapi
        self.location = self.llapi.location_check()
        if self.llapi.supervisor_check(): # Supervisors can see all contractors
            self.list_of_contractors, self.list_of_contractors_objects = self.llapi.get_contractor_list()
        else:                             # Employees on the otherhand get a list sorted by their location
            self.list_of_contractors, self.list_of_contractors_objects = self.llapi.sort_contractors_by_location(self.location)
        self.supervisor_options = ["Add new contractor"]
        self.employee_options = self.list_of_contractors
        self.splash_screen = """_____   __                   ____________        
___  | / /_____ _______      ___    |__(_)_______
__   |/ /_  __ `/_  __ \     __  /| |_  /__  ___/
_  /|  / / /_/ /_  / / /     _  ___ |  / _  /    
/_/ |_/  \__,_/ /_/ /_/      /_/  |_/_/  /_/     
                                                 """

    def add_new_contractor(self):         # First instantiates all info into a model class then sends it all the way to the storage layer
        self.llapi.clear_console()
        location = input("Enter location (Svalbard/Nuuk/Faroe Islands): ")
        contractor = input("Enter contractor (company name): ")
        name = input("Enter name: ")
        profession = input("Enter profession: ")
        phone_input = None
        while phone_input == None:
            try:
                phone_input = int(input("Enter phone number (without dialling code): "))
                if len(str(phone_input)) < 6:
                    print("Phone number entered is too short! Try again")
                    phone_input = None
                elif len(str(phone_input)) > 14:
                    print("Phone number entered is too long! Try again")
                    phone_input = None
            except ValueError:
                print(INVALID)
                phone_input =None
        if location.lower() == 'svalbard':
            phone = f'+47 {phone_input}'
        elif location.lower() == 'nuuk':
            phone = f'+299 {phone_input}'
        elif location.lower() == 'faroe islands':
            phone = f'+298 {phone_input}'
        opening_hours = input("Enter opening hours (hh:mm-hh:mm): ")
        rating = input("Enter rating(X/10): ")
        confirm = ""
        while confirm != "y" and confirm != "n":
            confirm = input("Confirm? (y/n): ")
            if confirm.lower() =='y':
                Contractor_mdl = contractors(contractor, name, profession, phone, opening_hours, location, rating)
                return self.llapi.add_new_contractor(Contractor_mdl)
            elif confirm.lower() == "n":
                return
            else:
                print(INVALID)

    def draw_options(self):               # Displays all the available options for the user
        self.llapi.clear_console()
        print(self.splash_screen)
        self.all_options = []
        self.all_options.extend(self.employee_options)
        if self.llapi.supervisor_check():
            self.all_options.extend(self.supervisor_options)
        print("=".center(70, '='))
        print("Contractors".center(70, ' '))
        print("=".center(70, '='))
        print()
        for index in self.all_options:
            if index == "Add new contractor":
                print()
            print(f"{str(self.all_options.index(index) + 1)+'.':<5} {index}")
        print("R.    Return\n")
        
    def prompt_input(self):               # Finds out what option the user wants with entered key.
        while True:
            self.draw_options()
            command = input("\tEnter an option: ")
            if self.llapi.supervisor_check() and command == str(self.all_options.index("Add new contractor")+1):
                self.add_new_contractor() # Supervisors can add a new contractor by entering the last number before the return option
                return
            elif command.lower() == 'r':
                return
            else:
                try:                      # Tries to call the model class' __string__
                    index = int(command) - 1
                    self.llapi.clear_console()
                    print(self.splash_screen)
                    print("=".center(48, '='))
                    print(self.list_of_contractors_objects[index].contractor.center(48, ' '))
                    print("=".center(48, '='))
                    print(self.list_of_contractors_objects[index])
                    input("\tEnter to continue")
                except:                   # Except when key is not found or index error
                    print("Invalid option, please try again.")
                    time.sleep(1)
        
        