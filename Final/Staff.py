from Customer import Customer

class Staff(Customer):
    def __init__(self):
        super().__init__()
        self.taxRate = 0.09
    

