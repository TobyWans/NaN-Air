import csv 
from src.models.destination import destination_info

class DestinationDL:
    def __init__(self):
        self.filepath = "data/Destinations.csv"

    def destination_info(self):
        ret_list = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                dest = destination_info(row["id_number"], row["airport"], row["country"], row["phone"], row["opening_hour"], row["closing_hour"], row["supervisor"])
                ret_list.append(dest)
        return ret_list