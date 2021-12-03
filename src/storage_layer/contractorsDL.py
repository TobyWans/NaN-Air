import csv
from src.models.contractors import contractors

class ContractorMenuDL:
    def __init__(self):
        self.contractor_file = 'src\data\Contractors.csv'

    def add_new_contractor(self, mdl):
        with open(self.contractor_file, 'a', newline='', encoding='utf-8') as contr_file:
            fieldnames = ['contractor','name','profession','phone','opening_hours','location','rating']
            writer = csv.DictWriter(contr_file, fieldnames=fieldnames)
            writer.writerow({'contractor':mdl.contractor, 'name':mdl.name, 'profession':mdl.profession, 'phone':mdl.phone, 'opening_hours':mdl.opening_hours, 'location':mdl.location, 'rating':mdl.rating})
            contr_file.close()
            return

    def get_contractor_list(self):
        first_run = True
        contractor_list = []
        with open(self.contractor_file, newline='', encoding='utf-8') as contr_file:
            reader = csv.DictReader(contr_file)
            for row in reader:
                if first_run != True:
                    contractor = contractors(**row)
                    contractor_list.append(contractor)
                first_run = False
            return contractor_list
