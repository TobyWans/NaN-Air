from ui_layer.login_checker import LogInCheck
import random

PRIORITY = ('low', 'medium', 'high')

class WorkRequestMenu:
    def __init__(self):
        random.seed(69)
        self.supervisor_options = ["Create new request", "Open/Change request", "Close request"]
        self.employee_options = ["All work requests", "Search by ID", "Search by date", "Your open requests", "Finished request"]
        self.go_back = "Q. Back"
    
    def draw_options(self):
        if LogInCheck.ID_login():
            for index in self.supervisor_options:
                print(index)
        else:
            for index in self.employee_options:
                print(index)
            
        
    def create_new_request(self):
        work_request_ID = print(f"Work request ID: {random.randint(100, 999)}")
        housing = input("Housing: ")
        description = input("Description: ")
        priority = input("Priority: ")
        if priority.lower not in PRIORITY:
            pass
    
    def close_request(self):
        pass