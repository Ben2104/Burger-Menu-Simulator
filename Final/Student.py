from Customer import Customer

class Student(Customer):
    def __init__(self):
        super().__init__()
        self.taxRate = 0
    
    def getTaxAmount(self, amount):
        return (amount * self.taxRate)
    def applyTax(self, amount):
        return (amount) + (amount * self.taxRate)
    

    
    