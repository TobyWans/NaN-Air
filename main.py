from src.logic_layer.LLAPI import LLAPI
from src.ui_layer.main_menu import MainMenu
import time, os


if __name__ == "__main__":
    running = True
    menu = MainMenu()
    while running:
        menu.login()
        inputs = menu.prompt_input()
        if inputs == 'q':
            quit_menu = input("Do you want to close the program?(Y/N): ")
            if quit_menu.lower() == 'y':
                clear_cmd = os.system('cls' if os.name in ('nt', 'dos') else 'clear')
                print("\n\n\n\n\n")
                print("""_____   __                   ____________        
___  | / /_____ _______      ___    |__(_)_______
__   |/ /_  __ `/_  __ \     __  /| |_  /__  ___/
_  /|  / / /_/ /_  / / /     _  ___ |  / _  /    
/_/ |_/  \__,_/ /_/ /_/      /_/  |_/_/  /_/     
=================================================""")
                time.sleep(2)
                clear_cmd = os.system('cls' if os.name in ('nt', 'dos') else 'clear')
                running = False
            else:
                pass