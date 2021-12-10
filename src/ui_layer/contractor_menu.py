from src.logic_layer.LLAPI import LLAPI
from src.models.contractors import contractors
import time

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
        if self.llapi.supervisor_check() == False:
            print()
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
                    print(("\n"*7),"\tInvalid option, please try again.")
                    time.sleep(1)
        

    def add_new_contractor(self):         # First instantiates all info into a model class then sends it all the way to the storage layer
        self.llapi.clear_console()        # Also checks for correct format on all inputs
        print(self.splash_screen)
        print("=".center(48, '='))
        print("Add a new contractor".center(48, ' '))
        print("=".center(48, '='))

        while True:                       # Location
            location = input("Enter location (Svalbard/Nuuk/Faroe Islands): ")
            if location.lower() != 'svalbard' and location.lower() != 'nuuk' and location.lower() != 'faroe islands':
                print("Invalid location! Try again")
            else:
                break
                                          # Contractor/company name
        contractor = input("Enter contractor (company name): ")

        name = None                       # Name
        while name == None:
            name = input("Enter name: ")
            for letter in name:
                if letter.isdigit():
                    print("Enter only letters!")
                    name = None
                    break

        profession = None                 # Profession
        while profession == None:
            profession = input("Enter profession: ")
            for letter in profession:
                if letter.isdigit():
                    print("Enter only letters!")
                    profession = None
                    break

        phone_input = None                # Phone number
        while phone_input == None:
            try:
                phone_input = int(input("Enter phone number (without dialling code): "))
                if len(str(phone_input)) < 6:
                    print("Phone number entered is too short!")
                    phone_input = None
                if len(str(phone_input)) > 14:
                    print("Phone number entered is too long!")
                    phone_input = None
            except ValueError:
                print("Enter only integers!")
                phone_input =None

        if location.lower() == 'svalbard': # Country code
            phone = f'+47 {phone_input}'
        elif location.lower() == 'nuuk':
            phone = f'+299 {phone_input}'
        elif location.lower() == 'faroe islands':
            phone = f'+298 {phone_input}'

        while True:                        # Opening hours
            opening_hours = input("Enter opening hours (hh:mm-hh:mm): ")
            try:
                if int(opening_hours[0:2]) in range(00,24) and int(opening_hours[3:5]) in range(0,60) and int(opening_hours[6:8]) in range(00,24) and int(opening_hours[9:11]) in range(0,60):
                    break
                else:
                    print("Invalid format!")
            except ValueError:
                print("Invalid value!") 

        while True:                       # Rating
            rating = input("Enter rating (X/10): ")
            if rating.isnumeric():
                if int(rating) <= 10 and int(rating) >= 0:
                    break
                else:
                    print("Rating is out of range!")
            else:
                print("Invalid rating!")

        confirm = ""                      # Confirm
        while confirm != "y" and confirm != "n":
            confirm = input("Confirm? (y/n): ")
            if confirm.lower() =='y':
                Contractor_mdl = contractors(contractor, name, profession, phone, opening_hours, location, rating)
                self.llapi.clear_console()
                print("\n\n\n\n\tContractor has been created. Refreshing list...")
                time.sleep(1.8)
                return self.llapi.add_new_contractor(Contractor_mdl)
            elif confirm.lower() == "n":
                return
            else:
                print("\n\tInvalid input. Try again!\n")