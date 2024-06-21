import datetime
from Order import *
from Burger import *
from Student import *
from Staff import * 
if __name__=="__main__":
    o = Order()
    o.displayMenu()
    curOrder = o.getOrder()
    curPrice = o.calculatePrice(curOrder)
    student = Student()
    staff = Staff()

    bill = o.display_bill(curOrder, curPrice, staff)
    o.saveToFile(bill)
    print(bill)