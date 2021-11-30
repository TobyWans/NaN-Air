from src.logic_layer.login_checker import LogInCheck


class LLAPI:
    def __init__(self):
        self.login_checker = LogInCheck()
        
    def ID_login(self, id):
        return self.login_checker.ID_login(id)
    
    def supervisor_check(self):
        return self.login_checker.supervisor_check()