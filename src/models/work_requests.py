class Work_Request:
    def __init__(self, req_id, title, where, housing_id, description, priority, status, date, user_id):
        self.req_id = req_id
        self.title = title
        self.where = where
        self.housing_id = housing_id
        self.description = description
        self.priority = priority
        self.status = status
        self.date = date
        self.user_id = user_id
        
    def __str__(self):
        return f"{'Date created:'} {self.date}\tID: {self.req_id}\n{'Title:':<13} {self.title}\n{'Where:':<13} {self.where}\n{'Housing:':<13} {self.housing_id}\n{'Description:'}\n{self.description_readability(self.description)}\n{'Priority:':<13} {self.priority}\n{'Status:':<13} {self.status}\n"
    
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