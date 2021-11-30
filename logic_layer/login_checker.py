# Þetta er bara til að prófa login, þurfum að búa til eh file með öllu starfsfólki
EMPLOYEE = {"joi": "1234", "chuck": "1111", "mike": "1221", "klaus": "1755", }

class LogInCheck:
    def __init__(self):
        pass
        
    # log in validation
    # kannski hægt að gera þetta auðveldara?
    def ID_login(self):
        while True:
            login = input("Enter your ID: ")
            if not login.isdecimal():
                print("Invalid ID")
            elif len(login) < 4:
                print("Invalid ID")
            else:
                search_ID = self.search(EMPLOYEE, login)
                if search_ID != None:
                    print(f"Welcome {search_ID}, ")
                    user_check = self.supervisor_check(login)
                    if user_check:
                        print("You're logged in as a supervisor")
                        return True
                    else:
                        print("You're logged in as an employee")
                        return False
                else:
                    print("Invalid ID")
            
    # spuring hvort við breytum starfsmanna skjali í dictonary til að nota þetta func?
    # leitar af id sem er tegnt við nafn í dict
    def search(self, values: dict, search: str):
        for name, id in values.items():
            if search in id:
                return name
        return None
    
    # skoðar hvort starfsmanna ID endar á 1 ef svo er þá er þetta supervisor
    def supervisor_check(self, user_id):
        if user_id[3] == '1':
            return True
        else:
            return False