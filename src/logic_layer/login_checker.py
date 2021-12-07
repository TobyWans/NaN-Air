# Þetta er bara til að prófa login, þurfum að búa til eh file með öllu starfsfólki
import uuid
from src.storage_layer.DLAPI import DLAPI

class LogInCheck:
    def __init__(self, dlapi: DLAPI):
        self.dlapi = dlapi
        self.current_user = None
        
        # log in validation
    def ID_login(self, login):
        self.user_id = login
        if not login.isdecimal():
            return False
        elif len(login) < 4:
            return False
        else:
            if self.dlapi.confirm_emp_login(login):
                
                return True
            else:
                return False
            
        # Searches for name by ID
    def search(self, values: dict, search: str):
        for name, id in values.items():
            if search in id:
                return name
        return None
    
        # Checks if employee ID ends with the number 1,
        # if so that user is a supervisor
    def supervisor_check(self):
        if self.user_id[3] == '1':
            return True
        else:
            return False
        
        # Random number generator for IDs
    def employee_rng_id(self):
        decimal = False
        while not decimal:
            rand_id = str(uuid.uuid4())[:4]
            if rand_id.isdecimal() and rand_id[3] != '1':
                decimal = True
            if rand_id.isdecimal() and rand_id in self.dlapi.get_logins():
                decimal = False
        self.dlapi.login_writer(rand_id)
        return rand_id

        # Random number generator for supervisor IDs
    def supervisor_rng_id(self):
        decimal = False
        while not decimal:
            rand_id = str(uuid.uuid4())[:3]
            if rand_id.isdecimal():
                decimal = True
            if rand_id.isdecimal() and rand_id + '1' in self.dlapi.get_logins():
                decimal = False
        self.dlapi.login_writer(rand_id + '1')
        return rand_id + '1'