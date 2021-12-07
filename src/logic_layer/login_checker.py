# Þetta er bara til að prófa login, þurfum að búa til eh file með öllu starfsfólki
import uuid
from src.storage_layer.DLAPI import DLAPI

class LogInCheck:
    def __init__(self, dlapi: DLAPI):
        self.dlapi = dlapi
        self.current_user = None
        
    # log in validation
    # kannski hægt að gera þetta auðveldara?
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
            
    # spuring hvort við breytum starfsmanna skjali í dictonary til að nota þetta func?
    # leitar af id sem er tegnt við nafn í dict
    def search(self, values: dict, search: str):
        for name, id in values.items():
            if search in id:
                return name
        return None
    
    # skoðar hvort starfsmanna ID endar á 1 ef svo er þá er þetta supervisor
    def supervisor_check(self):
        if self.user_id[3] == '1':
            return True
        else:
            return False
        
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