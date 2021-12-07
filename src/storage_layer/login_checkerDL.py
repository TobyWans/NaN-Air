class LoginCheckerDL:
    def __init__(self):
        self.filepath = 'src/data/loginID.txt'
        
        # Reads the LoginID text file and puts them in a list
    def get_logins(self):
        with open(self.filepath, 'r', newline='') as logins:
            lines = logins.read().split('\n')
            logins.close
        return lines
    
        # Writes new IDs to the LoginID text file
    def login_writer(self, emp_id):
        with open(self.filepath, 'a', newline='') as logins:
            logins.write(emp_id + '\n')
            logins.close