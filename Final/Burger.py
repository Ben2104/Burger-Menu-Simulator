class Burger:
    price = 0
    name = ""
    amount = 0
    
    def __init__(self, newPrice, newName):
        self.price = newPrice
        self.name = newName
        
    def setAmount(self, newAmount):
        self.amount = newAmount
    
    def incrementAmount(self):
        self.amount += 1
    
    def getAmount(self):
        return self.amount

    def getPrice(self):
        return self.price * self.amount
    
    def getName(self):
        return self.name
    
