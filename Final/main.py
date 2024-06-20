from Order import *
from Burger import *
def main():
    o = Order()
    currentOrder = o.getOrder()
    currentPrice = o.calculatePrice(currentOrder)
    o.display_bill(currentOrder, currentPrice)
    
main()