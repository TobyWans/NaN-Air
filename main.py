


from ui_layer.employee_menu import EmployeeMenu
from ui_layer.login_checker import LogInCheck
from ui_layer.supervisor_menu import SupervisorMenu


if __name__ == "__main__":
    login = LogInCheck()
    if login.ID_login():
        supervisor = SupervisorMenu()
        supervisor.draw_options()
    else:
        employee = EmployeeMenu()
        employee.draw_options()
    