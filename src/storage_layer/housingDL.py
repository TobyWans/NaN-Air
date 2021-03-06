import csv

from src.models.housing import Housing
from src.models.housing import Particular_real_estate

class HousingDL:
    def __init__(self):
        self.filepath = "src/data/Housing.csv"

    def add_housing(self, hous): #Gets new housing and write it to choosen file
        with open(self.filepath, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["supervisor", "property_number" ,"street_name" ,"street_number", "location" ,"size_in_m2", "nr_of_rooms" ,"type", "requires_maintenance", "rental_status"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({"supervisor": hous.supervisor,"property_number": hous.property_number, "street_name": hous.street_name, "street_number": hous.street_number, "location": hous.location, "size_in_m2": hous.size_in_m2, "nr_of_rooms": hous.nr_of_rooms, "type": hous.type, "requires_maintenance": hous.requires_maintenance, "rental_status": hous.rental_status})
    
    def change_housing(self, id_number, changed_hous): #gets id number of house which should be changed, reed the file, finds the right hous,  and then write to the file with changes
        change_list = list()
        with open(self.filepath, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                
                if str(id_number) == row['property_number']:
                    change_list.append({"supervisor": changed_hous.supervisor,"property_number": changed_hous.property_number, "street_name": changed_hous.street_name, "street_number": changed_hous.street_number, "location": changed_hous.location, "size_in_m2": changed_hous.size_in_m2, "nr_of_rooms": changed_hous.nr_of_rooms, "type": changed_hous.type, "requires_maintenance": changed_hous.requires_maintenance, "rental_status": changed_hous.rental_status})
                else:
                    change_list.append(row)
                    
        with open(self.filepath, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["supervisor", "property_number" ,"street_name" ,"street_number", "location" ,"size_in_m2", "nr_of_rooms" ,"type", "requires_maintenance", "rental_status"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer2 = csv.writer(csvfile)
            writer2.writerow(fieldnames)
            writer.writerows(change_list)

    def get_housing_list(self): #gets list of all houses
            hous_list = []
            with open(self.filepath, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    hous_list.append(row)
            return hous_list
        
    def get_housing_id_by_location(self, location): #get list of houses with choosen location
        housing_id_list = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['location'] == location:
                    housing_id = Housing(**row)
                    housing_id_list.append(housing_id)
        return housing_id_list
    
    def get_location_list(self): #get list of locaation
        location_list = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['location'] in location_list: 
                    continue
                else:
                    location_list.append(row['location'])
        return location_list
    
    def search_by_housing_id(self, entered_property_number): #if given property number is founded, returns information about property, else return None
        
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["property_number"].lower() == entered_property_number.lower():
                    property = Particular_real_estate(**row)
                    return property
            return None

    def get_rental_status(self):
        #List of free to book and booked requests
        free_to_book = []
        booked = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                    hous = Housing(**row)
                    if row['rental_status'] == 'free to rent':
                        free_to_book.append(hous)
                    elif row['rental_status'] == 'booked':
                        booked.append(hous)
        return free_to_book, booked

    def get_rental_status_by_location(self, user_location): 
        #List of free to book and booked requests for given location
        free_to_book = []
        booked = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['location'] == user_location:
                    hous = Housing(**row)
                    if row['rental_status'] == 'free to rent':
                        free_to_book.append(hous)
                    elif row['rental_status'] == 'booked':
                        booked.append(hous)
                    
        return free_to_book, booked

    