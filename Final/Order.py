from Burger import *
class Order:
    def __init__(self):
        self._priceBtax = 0
        self._priceAtax = 0
        self._tax = 0.0825
        self.deAnza = Burger("De Anza Burger", 5.25)
        self.baconCheese = Burger("Bacon Cheese", 5.75)
        self.mushroomSwiss = Burger("Mushroom Swiss", 5.95)
        self.western = Burger("Western Burger", 5.95)
        self.donCali = Burger("Don Cali Burger", 5.95)
        
        self._priceDict = {
                1: (self.deAnza.getName(), self.deAnza.getPrice()),
                2: (self.baconCheese.getName(), self.baconCheese.getPrice()),
                3: (self.mushroomSwiss.getName(), self.mushroomSwiss.getPrice()),
                4: (self.western.getName(), self.western.getPrice()),
                5: (self.donCali.getName(), self.donCali.getPrice())
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
            choice = input("Enter the number of the item you want (or '6' to exit): ").strip()
            if choice == '6':
                return None
            elif not choice.isdigit() or int(choice) not in range(1, 6):
                print("Invalid input. Please enter a number between 1 and 5.")
                continue
            else:
                quantity = input(f"How many {self._priceDict[int(choice)][0]} do you want? ").strip()
                if not quantity.isdigit() or int(quantity) < 1:
                    print("Invalid quantity. Please enter a positive integer.")
                    continue
                order[int(choice)] = int(quantity)
                another = input("Do you want to order anything else? (yes/no): ").strip().lower()
                if another != "yes":
                    return order

    def calculatePrice(self, order):
        """Calculate the total price of the order."""
        total_price = sum(self._priceDict[item][1] * quantity for item, quantity in order.items())
        return total_price
    
    def applyTax(total_price, customer):
        """Apply tax based on user type."""
        if customer.isStudent():
            return total_price
        elif not customer.isStudent():
            tax = total_price * 0.09
            return total_price + tax
        else:
            return "Invalid user type."
        
    def display_bill(order, total_price, customer):
        """Display the bill including item details, total before tax, tax amount, and total price after tax."""
        print("Bill:")
        for item, quantity in order.items():
            item_name, price = self._priceDict[item]
            print(f"{item_name}: {quantity} x ${price:.2f} = ${price * quantity:.2f}")
            
        print(f"Total before tax: ${total_price:.2f}")
        
        if not customer.isStudent():
            tax = total_price * 0.09
            print(f"Tax amount: ${tax:.2f}")
            total_price += tax
        print(f"Total price after tax: ${total_price:.2f}")
