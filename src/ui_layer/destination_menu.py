from src.logic_layer.LLAPI import LLAPI


class DestinationMenu:
    def __init__(self, llapi):
        # random.seed(69)
        self.llapi = llapi
        self.supervisor_options = ["Nuuk, Grænland", "Kulusuk, Grænland", "Þórshöfn, Færeyjar", "Tingwall, Hjaltlandseyjum", "Longyearbyen, Svalbarði"]

    def draw_options(self):
        self.llapi.clear_console()
        all_options = []
        all_options.extend(self.supervisor_options)
        for index in all_options:
            print(f"\t{all_options.index(index) + 1}. {index}")
        print("\tQ. Return\n")
        return self.prompt_input()

    def prompt_input(self):
        while True:
            command = input("Enter an option: ")
            print_destination = self.llapi.destination_info()
            dest_str_list = []
            for dest in print_destination:
                dest_str_list.append(dest)
            if command == "1":
                print(dest_str_list[0])
            elif command  == "2":
                print(dest_str_list[1])
            elif command  == "3":
                print(dest_str_list[2])
            elif command  == "4":
                pass
            elif command  == "5":
                pass

    