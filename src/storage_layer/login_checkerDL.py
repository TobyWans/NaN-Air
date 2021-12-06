class LoginCheckerDL:
    def __init__(self):
        self.filepath = 'src/data/loginID.txt'
        
    def get_logins(self):
        with open(self.filepath, 'r', newline='') as logins:
            lines = logins.read().split('\n')
            logins.close
        return lines
    
    def login_writer(self, emp_id):
        with open(self.filepath, 'a', newline='') as logins:
            logins.write(emp_id + '\n')
            logins.close