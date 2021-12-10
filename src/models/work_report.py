class Work_Report:
    def __init__(self, rep_id, housing, regular_irr, description, time, contractor, other, employee):
        self.rep_id = rep_id
        self.housing = housing
        self.regular_irr = regular_irr
        self.desc = description
        self.time = time
        self.contractor = contractor
        self.other = other
        self.employee = employee
                
    def __str__(self):
        return f"Work Request ID: {self.rep_id}\n{'Housing ID:':<13} {self.housing}\n{'Regular/Irregular Maintenance:':<13} {self.regular_irr}\n{'Description:'}\n{self.description_readability(self.desc)}\n{'Time:':<13} {self.time}\n{'Contractor costs:':<13} {self.contractor}\n{'Other costs:':<13} {self.other}\n{'Employee ID:':<13} {self.employee}"
    
        # Code to make the description more readable
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