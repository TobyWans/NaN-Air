class Destination:
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

    