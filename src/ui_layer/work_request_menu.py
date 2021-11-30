from src.logic_layer.LLAPI import LLAPI
import random

PRIORITY = ('low', 'medium', 'high')

class WorkRequestMenu:
    def __init__(self):
        random.seed(69)
        self.LLAPI = LLAPI()
        self.supervisor_options = ["Create new request", "Open/Change request", "Close request"]
        self.employee_options = ["All work requests", "Search by ID", "Search by date", "Your open requests", "Finished request"]
        self.go_back = "Q. Back"
    
    def draw_options(self):
        all_options = []
        all_options.extend(self.employee_options)
        if self.LLAPI.supervisor_check():
            all_options.extend(self.supervisor_options)
        for index in all_options:
            print(f"\t{all_options.index(index) + 1}. {index}")
        print("\tQ. Log out\n")
            
        
    def create_new_request(self):
        work_request_ID = print(f"Work request ID: {random.randint(100, 999)}")
        housing = input("Housing: ")
        description = input("Description: ")
        priority = input("Priority: ")
        if priority.lower not in PRIORITY:
            pass
    
    def close_request(self):
        pass