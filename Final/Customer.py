class Customer:
    def __init__(self):
        return
    
    def getTaxAmount(self, amount):
        return NotImplemented

    def applyTax(self, amount):
        raise NotImplemented
    def isStudent(self, user_type):
        if (user_type == "student"):
            return True
        else:
            return False