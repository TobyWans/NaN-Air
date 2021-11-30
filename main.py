from src.ui_layer.main_menu import MainMenu





if __name__ == "__main__":
    menu = MainMenu()
    menu.draw_options()
    
    # login = LogInCheck()
    # if login.ID_login():
    #     supervisor = SupervisorMenu()
    #     supervisor.draw_options()
    # else:
    #     employee = EmployeeMenu()
    #     employee.draw_options()