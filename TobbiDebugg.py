from src.logic_layer.LLAPI import LLAPI
from src.ui_layer.main_menu import MainMenu


if __name__ == "__main__":
    running = True
    menu = MainMenu()
    while running:
        menu.login()
        inputs = menu.prompt_input()
        if inputs == 'q':
            quit_menu = input("Do you want to close the program?(Y/N)")
            if quit_menu.lower() == 'y':
                running = False
            else:
                pass