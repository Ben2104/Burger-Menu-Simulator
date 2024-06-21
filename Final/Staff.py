from Customer import Customer

class Staff(Customer):
    def __init__(self):
        super().__init__()
        self.taxRate = 0.09
    
    def getTaxAmount(self, amount):
        return self.taxRate * amount

    def applyTax(self, amount):
        return (amount) + (amount * self.taxRate)
    

