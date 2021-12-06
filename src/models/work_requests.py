class Work_Request:
    def __init__(self, id, title, where, housing_id, description, priority, status, date):
        self.id = id
        self.title = title
        self.where = where
        self.housing_id = housing_id
        self.description = description
        self.priority = priority
        self.status = status
        self.date = date
        
    def __str__(self):
        return f"Date created: {self.date}\tID: {self.id}\nTitle: {self.title}\nWhere: {self.where}\nHousing: {self.housing_id}\nDescription:\n{self.description_readability(self.description)}\nPriority: {self.priority}\nStatus: {self.status}\n"
    
    def description_readability(self, desc):
        desc_list = list()
        count = 0
        for letter in desc:
            count += 1
            desc_list.append(letter)
            if count >= 80 and letter == ' ':
                desc_list.append('\n')
                count = 0
        return ''.join(desc_list)