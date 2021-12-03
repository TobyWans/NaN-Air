# Þetta er bara til að prófa login, þurfum að búa til eh file með öllu starfsfólki
import uuid

class LogInCheck:
    def __init__(self):
        self.emp_dict = {"joi": "1234", "chuck": "1111", "mike": "1221", "klaus": "1755", }
        
    # log in validation
    # kannski hægt að gera þetta auðveldara?
    def ID_login(self, login):
        self.user_id = login
        if not login.isdecimal():
            return False
        elif len(login) < 4:
            return False
        else:
            search_ID = self.search(self.emp_dict, login)
            if search_ID != None:
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
        
    def rng_id(self):
        decimal = False
        while not decimal:
            rand_id = str(uuid.uuid4())[:4]
            if rand_id.isdecimal():
                decimal = True
        return rand_id
    
    
    
    
    
    
        # generate uuid
        # if uuid contains a letter
        # regenerate until there are no letters.
        # return uuid with only numbers