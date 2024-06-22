class Customer:
    def __init__(self):
        return
    
    def getTaxAmount(self, amount):
        return self.taxRate * amount

    def applyTax(self, amount):
        return (amount) + (amount * self.taxRate)
    def isStudent(self, user_type):
        if (user_type == "student"):
            return True
        else:
            return False