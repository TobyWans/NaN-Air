from ui_layer.login_checker import LogInCheck
import random


class WorkRequestMenu:
    def __init__(self):
        random.seed(69)
        self.supervisor_options = """
Work requests:
        1. Create new request
        2. Open/Change request
        3. Close request
        Q. Back
        """
        self.employee_options = """
Work requests:
        1. All work requests
        2. Search by ID
        3. Search by date
        4. Your open requests
        5. Finished request
        Q. Back
        """
    
    def draw_options(self):
        if LogInCheck.ID_login(): print(self.supervisor_options)
        else: print(self.employee_options)
        
    def create_new_request(self):
        work_request_ID = print(f"Work request ID: {random.randint(100, 999)}")
    
    def close_request(self):
        pass