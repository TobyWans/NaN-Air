import csv
from src.models.contractors import contractors

class ContractorMenuDL:
    def __init__(self):
        self.contractor_file = 'src\data\Contractors.csv'

    def add_new_contractor(self, Mdl):                  # Uses the csv dict reader to write the model into the csv file
        with open(self.contractor_file, 'a', newline='', encoding='utf-8') as contr_file:
            fieldnames = ['contractor','name','profession','phone','opening_hours','location','rating']
            writer = csv.DictWriter(contr_file, fieldnames=fieldnames)
            writer.writerow({'contractor':Mdl.contractor, 'name':Mdl.name, 'profession':Mdl.profession, 'phone':Mdl.phone, 'opening_hours':Mdl.opening_hours, 'location':Mdl.location, 'rating':Mdl.rating})
            return

    def get_contractor_list(self):                      # Turns each row of the csv file into the model's class object. Returns a list of all of them
        contractor_list = []
        with open(self.contractor_file, newline='', encoding='utf-8') as contr_file:
            reader = csv.DictReader(contr_file)
            for row in reader:
                Contractor = contractors(**row)
                contractor_list.append(Contractor)
            return contractor_list
        
    def sort_contractors_by_location(self, location):   # Does the same as get_contractor_list but only when user's location matches
        sorted_list = []
        with open(self.contractor_file, newline='', encoding='utf-8') as contr_file:
            reader = csv.DictReader(contr_file)
            for row in reader:
                if row['location'] == location:
                    contractor = contractors(**row)
                    sorted_list.append(contractor)
        return sorted_list
