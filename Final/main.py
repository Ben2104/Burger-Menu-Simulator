from Order import *
from Burger import *
from Student import *
from Staff import * 
def main():
    o = Order()
    o.displayMenu()
    curOrder = o.getOrder()
    curPrice = o.calculatePrice(curOrder)
    student = Student()
    staff = Staff()

    o.display_bill(curOrder, curPrice, staff)
main()