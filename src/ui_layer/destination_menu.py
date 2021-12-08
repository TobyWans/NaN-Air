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
            print(f"\t{all_options.index(index) + 1}. {index}")          # Prints all the available options i.e the destinations.
        print("\tR. Return\n")

    def prompt_input(self):          # prompts for input and prints the corresponding info.
        while True:
            self.draw_options()
            command = input("Enter an option: ")

            dest_list = self.llapi.destination_info()          # The info.

            if command == "1":
                search_city = self.llapi.search_des_file_by_city("Nuuk")
                if search_city == None:
                    print("Sorry, there's no information about this destination")
                    time.sleep(1)
                else:
                    print("-".center(48, '-'))
                    print("Nuuk".center(48, ' '))
                    print("-".center(48, '-'))
                    print(dest_list[0])
                    back = input("Press enter to continue")
                    self.llapi.clear_console()
            elif command  == "2":
                search_city = self.llapi.search_des_file_by_city("Tórshavn")
                if search_city == None:
                    print("Sorry, there's no information about this destination")
                    time.sleep(1)
                else:
                    print("-".center(48, '-'))
                    print("Tórshavn".center(48, ' '))
                    print("-".center(48, '-'))
                    print(dest_list[1])
                    back = input("Press enter to continue")
                    self.llapi.clear_console()
            elif command  == "3":
                search_city = self.llapi.search_des_file_by_city("Longyearbyen")
                if search_city == None:
                    print("Sorry, there's no information about this destination")
                    time.sleep(1)
                else:
                    print("-".center(48, '-'))
                    print("Longyearbyen".center(48, ' '))
                    print("-".center(48, '-'))
                    print(dest_list[2])
                    back = input("Press enter to continue")
                    self.llapi.clear_console()
            elif command  == "4":
                search_city = self.llapi.search_des_file_by_city("Kulusuk")
                if search_city == None:
                    print("Sorry, there's no information about this destination")
                    time.sleep(1)
                else:
                    print("-".center(48, '-'))
                    print("Kulusuk".center(48, ' '))
                    print("-".center(48, '-'))
                    print(dest_list[3])
                    back = input("Press enter to continue")
                    self.llapi.clear_console()
            elif command  == "5":
                search_city = self.llapi.search_des_file_by_city("Tingwall")
                if search_city == None:
                    print("Sorry, there's no information about this destination")
                    time.sleep(1)
                else:
                    print("-".center(48, '-'))
                    print("Tingwall".center(48, ' '))
                    print("-".center(48, '-'))
                    print(dest_list[4])
                    back = input("Press enter to continue")
                    self.llapi.clear_console()
            elif command.lower() == 'r':
                self.llapi.clear_console()
                return 'r'
            else:
                print("Invalid option, please try again ")
                time.sleep(1)

    