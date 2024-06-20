class Burger:
    def __init__(self, newName, newPrice):
        self.price = newPrice
        self.name = newName
        
    def setAmount(self, newAmount):
        self.amount = newAmount
    
    def incrementAmount(self):
        self.amount += 1
    
    def getAmount(self):
        return self.amount

    def getPrice(self):
        return self.price
    
    def getName(self):
        return self.name
    
