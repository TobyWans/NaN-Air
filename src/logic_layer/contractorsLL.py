from src.storage_layer.DLAPI import DLAPI
from src.models.contractors import contractors


class ContractorMenuLL:
    def __init__(self, dlapi):
        self.dlapi = dlapi
    
    def add_new_contractor(self):
        contractor = input("Enter contractor: ")
        name = input("Enter name: ")
        profession = input("Enter profession: ")
        phone = input("Enter phone: ")
        opening_hours = input("Enter opening hours: ")
        location = input("Enter location: ")
        rating = input("Enter rating: ")
        contractor_mdl = contractors(contractor, name, profession, phone, opening_hours, location, rating)
        self.dlapi.add_new_contractor(contractor_mdl)

    def get_contractor_list(self):
        contractor_list = self.dlapi.get_contractor_list()
        self.contractor_list_str = []
        for contractor in contractor_list:
            contr_str = contractor.display()
            self.contractor_list_str.append(contr_str)
        return self.contractor_list_str, contractor_list