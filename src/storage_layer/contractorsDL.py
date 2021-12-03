import csv
from src.models.contractors import contractors

class ContractorMenuDL:
    def __init__(self):
        self.contractor_file = 'src\data\Contractors.csv'

    def add_new_contractor(self):
        pass

    def get_contractor_list(self):
        first_run = True
        contractor_list = []
        with open(self.contractor_file, newline='', encoding='utf-8') as contr_file:
            reader = csv.reader(contr_file)
            for row in reader:
<<<<<<< Updated upstream
                if first_run != True:
                    contractor = contractors(*row)
                    contractor_list.append(contractor)
                first_run = False
            return contractor_list
=======
                pass
>>>>>>> Stashed changes
