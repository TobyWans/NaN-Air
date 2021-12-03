import csv
from src.models.contractors import contractors

class ContractorMenuDL:
    def __init__(self):
        self.contractor_file = 'src\data\Contractors.csv'

    def add_new_contractor(self):
        pass

    def get_contractor_list(self):
        contractor_list = []
        with open(self.contractor_file, newline='', encoding='utf-8') as contr_file:
            reader = csv.DictReader(contr_file)
            for row in reader:
                if 