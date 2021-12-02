from src.storage_layer.DLAPI import DLAPI
from src.models.contractors import contractors

class ContractorMenuLL:
    def __init__(self, dlapi): # Þörf á init?
        self.dlapi = dlapi
        self.contractor = []
        self.contractors_list = []

    def add_new_contractor(self): # talar við DLAPI
        pass

    def get_contractor_list(self): # líka
        pass