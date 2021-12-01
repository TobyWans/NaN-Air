from src.storage_layer.destinationDL import DestinationDL

class DLAPI:
    def __init__(self):
        self.destDL = DestinationDL()

    def destination_info(self):
        return self.destDL.destination_info()

    def create_new_employee(self):
        pass

    def change_employee(self):
        pass

    def get_all_employees(self):
        pass

    def search_employee_by_id(self):
        pass

    def search_employee_by_location(self):
        pass
