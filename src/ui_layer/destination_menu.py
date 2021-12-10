from src.logic_layer.LLAPI import LLAPI
import time


class DestinationMenu:
    def __init__(self, llapi: LLAPI):
        self.llapi = llapi
        self.supervisor_options = ["Nuuk, Greenland", "Tórshavn, Faroe Islands", "Longyearbyen, Svalbard", "Kulusuk, Greenland", "Tingwall, Shetland Islands"]
        self.splash_screen = """_____   __                   ____________        
___  | / /_____ _______      ___    |__(_)_______
__   |/ /_  __ `/_  __ \     __  /| |_  /__  ___/
_  /|  / / /_/ /_  / / /     _  ___ |  / _  /    
/_/ |_/  \__,_/ /_/ /_/      /_/  |_/_/  /_/     
                                                 """

    def draw_options(self):          # Draws up the Destination menu.
        self.llapi.clear_console()
        print(self.splash_screen)
        all_options = []
        all_options.extend(self.supervisor_options)
        print("=".center(48, '='))
        print("Destination Menu".center(48, ' '))
        print("=".center(48, '='))
        print()
        for index in all_options:
            print(f"\t\t{all_options.index(index) + 1}. {index}")          # Prints all the available options i.e the destinations.
        print("\t\tR. Return\n")

    def prompt_input(self):          # prompts for input and prints the corresponding info.
        while True:
            self.draw_options()
            command = input("\tEnter an option: ")        
            if command == "1":              # Info about Nuuk
                counter = 0
                self.display_info(counter)
            elif command  == "2":          # Info about Tórshavn
                counter = 1
                self.display_info(counter)
            elif command  == "3":          # Info about Longyearbyen
                counter = 2
                self.display_info(counter)
            elif command  == "4":          # Info about Kulusuk
                counter = 3
                self.display_info(counter)
            elif command  == "5":          # Info about tingwall
                counter = 4
                self.display_info(counter)
            elif command.lower() == 'r':          # returns to Main menu
                self.llapi.clear_console()
                return 'r'
            else:
                print("Invalid option, please try again ")
                time.sleep(1)
            
    def display_info(self, counter):        
        city_list =  self.llapi.get_only_city()
        city = city_list[counter]
        print("-".center(48, '-'))
        print(f"{city}".center(48, ' '))
        print("-".center(48, '-'))
        print(self.llapi.search_des_file_by_city(city))
        input("Press enter to continue")
        self.llapi.clear_console()