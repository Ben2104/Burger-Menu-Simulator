import datetime
import time
from Burger import *

class Order:
    def __init__(self):
        self.deAnza = Burger("De Anza Burger", 5.25)
        self.baconCheese = Burger("Bacon Cheese", 5.75)
        self.mushroomSwiss = Burger("Mushroom Swiss", 5.95)
        self.western = Burger("Western Burger", 5.95)
        self.donCali = Burger("Don Cali Burger", 5.95)
        
        self._priceDict = {
                1: (self.deAnza.getName(), float(self.deAnza.getPrice())),
                2: (self.baconCheese.getName(), float(self.baconCheese.getPrice())),
                3: (self.mushroomSwiss.getName(), float(self.mushroomSwiss.getPrice())),
                4: (self.western.getName(), float(self.western.getPrice())),
                5: (self.donCali.getName(), float(self.donCali.getPrice()))
        }
    
    def displayMenu(self):
        """Display the food menu with options and prices."""
        print("Menu:")
        for option, (item, price) in self._priceDict.items():
            print(f"{option}. {item}: ${price:.2f}")
        
    def getOrder(self):
        """Get user's order and quantity."""
        order = {}
        while True:
            choice = input("Enter the number of the item you want (or '6' to exit, '7' to clear): ").strip()
            if choice == '6':
                return None
            elif choice == '7':
                for key, val in order.items():
                    order[key] = 0
                print("Order cleared")
            elif not choice.isdigit() or int(choice) not in range(1, 7):
                print("Invalid input. Please enter a number between 1 and 5.")
                continue
            else:
                quantity = input(f"How many {self._priceDict[int(choice)][0]} do you want? ").strip()
                if not quantity.isdigit() or int(quantity) < 1:
                    print("Invalid quantity. Please enter a positive integer.")
                    continue
                if int(choice) not in order:
                    order[int(choice)] = int(quantity)
                else:
                    order[int(choice)] += int(quantity)
                another = input("Do you want to order anything else? (yes/no): ").strip().lower()
                if another != "yes":
                    return order

    def calculatePrice(self, order):
        """Calculate the total price of the order."""
        total_price = sum(self._priceDict[item][1] * quantity for item, quantity in order.items())
        return total_price
        
    def display_bill(self, order, total_price, customer):
        """Display the bill including item details, total before tax, tax amount, and total price after tax."""
        bill = "Bill:\n"
        for item, quantity in order.items():
            item_name, price = self._priceDict[item]
            bill += f"{item_name}: {quantity} x ${price:.2f} = ${price * quantity:.2f}\n"
            
        bill += f"Total before tax: ${total_price:.2f}\n"
        
        bill += f"Tax amount: ${customer.getTaxAmount(total_price):.2f}\n"
        bill += f"Total price after tax: ${customer.applyTax(total_price):.2f}\n"
        return bill
    
    def saveToFile(self, bill):
        timeStamp = time.time()
        orderTimeStamp = datetime.datetime.fromtimestamp(timeStamp).strftime('%Y-%m-%d %H-%M-%S')
        with open(orderTimeStamp, 'w') as outFile:
            outFile.write(bill)
            