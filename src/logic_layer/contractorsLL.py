from src.storage_layer.DLAPI import DLAPI
from src.models.contractors import contractors


class ContractorMenuLL:
    def __init__(self, dlapi):
        self.dlapi = dlapi
        self.contractor = []
        self.contractors_list = []

    def add_new_contractor(self): # talar við DLAPI
        pass

    def get_contractor_list(self): # líka
        contractor_list = self.dlapi.get_contractor_list()
        self.contractor_list_str = []
        for contractor in contractor_list:
            contr_str = contractor.display()
            self.contractor_list_str.append(contr_str)
        return self.contractor_list_str, contractor_list