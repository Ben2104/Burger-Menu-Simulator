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
    
    customer = Customer()
    user_type = input("Are you a student or a staff? ").strip().lower()
    
    if (customer.isStudent(user_type)):
        customer_type = Student()
    else:
        customer_type = Staff()
    
    bill = o.display_bill(curOrder, curPrice, customer_type)
    o.saveToFile(bill)
    print(bill)