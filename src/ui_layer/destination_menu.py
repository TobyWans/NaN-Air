from src.logic_layer.LLAPI import LLAPI


class DestinationMenu:
    def __init__(self, llapi: LLAPI):
        self.llapi = llapi
        self.supervisor_options = ["Nuuk, Grænland", "Þórshöfn, Færeyjar", "Longyearbyen, Svalbarði", "Kulusuk, Grænland", "Tingwall, Hjaltlandseyjum"]

    def draw_options(self):
        self.llapi.clear_console()
        all_options = []
        all_options.extend(self.supervisor_options)
        for index in all_options:
            print(f"\t{all_options.index(index) + 1}. {index}")
        print("\tR. Return\n")

    def prompt_input(self):
        while True:
            self.draw_options()
            command = input("Enter an option: ")
            print_destination = self.llapi.destination_info()
            if command == "1":
                print(print_destination[0])
                back = input("Press enter to continue")
                self.llapi.clear_console()
            elif command  == "2":
                print(print_destination[1])
                back = input("Press enter to continue")
                self.llapi.clear_console()
            elif command  == "3":
                print(print_destination[2])
                back = input("Press enter to continue")
                self.llapi.clear_console()
            elif command  == "4":
                pass
            elif command  == "5":
                pass
            elif command.lower() == 'r':
                self.llapi.clear_console()
                return 'r'
            else:
                print("Invalid option, please try again ")

    