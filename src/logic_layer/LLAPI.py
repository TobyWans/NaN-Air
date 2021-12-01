from src.logic_layer.login_checker import LogInCheck
from src.logic_layer.destinationLL import DestinationLL
from src.storage_layer.DLAPI import DLAPI
import os


class LLAPI:
    def __init__(self):
        self.login_checker = LogInCheck()
        self.destinationLL = DestinationLL(self.dlapi)
        self.dlapi = DLAPI()
        
    def ID_login(self, id):
        return self.login_checker.ID_login(id)
    
    def supervisor_check(self):
        return self.login_checker.supervisor_check()
    
    def clear_console(self):
        clear_cmd = os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        return clear_cmd

    def destination_info(self, index):
        return self.destinationLL.destination_info(index)