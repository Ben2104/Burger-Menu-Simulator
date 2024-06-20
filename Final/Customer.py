class Customer:
    def __init__(self, name):
        self.name = name

    def get_tax_rate(self):
        return 0.09  
    
    def applyTax(total_price, customer):
        """Apply tax based on user type."""
        if customer.isStudent():
            return total_price
        elif not customer.isStudent():
            tax = total_price * 0.09
            return total_price + tax
        else:
            return "Invalid user type."