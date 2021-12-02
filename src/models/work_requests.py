class Work_Request:
    def __init__(self, id, title, where, housing_id, description, priority):
        self.id = id
        self.title = title
        self.where = where
        self.housing_id = housing_id
        self.description = description
        self.priority = priority
        
    def __str__(self):
        return f"ID: {self.id}\nTitle: {self.title}\nWhere: {self.where}\nHousing: {self.housing_id}\nDescription:\n{self.description}\nPriority: {self.priority}\n"