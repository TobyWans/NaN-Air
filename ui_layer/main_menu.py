from logic_layer.Employee_logIn import LogIn

MENU = """1. Work Request
2. Contractors
3. Housing
Q. Log Out"""

# Þetta er bara til að prófa login, þurfum að búa til eh file með öllu starfsfólki
EMPLOYEE = {"joi": "1234", "chuck": "1111", "mike": "1221", "klaus": "1755", }

class MainMenu:
    def __init__(self):
        self.options = MENU
        
        
    def show_options(self):
        print(self.options)
        
    def ID_login(self):
        running = True
        while running:
            # try:
            login = input("Enter your ID: ")
            if not login.isdecimal():
                print("Invalid ID")
            elif len(login) < 4:
                print("Invalid ID")
            else:
                search_ID = self.search(EMPLOYEE, login)
                if search_ID != None:
                    print(f"Welcome {search_ID}")
                    user_check = self.supervisor_check(login)
                    running = False
                else:
                    print("Invalid ID")
            # except ValueError:
            #     print("Invalid ID")
            
    def search(self, values: dict, search: str):
        for key, value in values.items():
            if search in value:
                return key
        return None
    
    def supervisor_check(self, user):
        pass