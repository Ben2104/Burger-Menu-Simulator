import datetime
from Order import *
from Burger import *
from Student import *
from Staff import * 
if __name__=="__main__":
    flag = True 

    while flag:
        o = Order()
        o.displayMenu()
        curOrder = o.getOrder()
        if (curOrder == False):
            break
        curPrice = o.calculatePrice(curOrder)
        
        customer = Customer()
        user_type = input("Are you a student or a staff? ").strip().lower()
        
        if (customer.isStudent(user_type)):
            customer_type = Student()
        else:
            customer_type = Staff()
        
        bill = o.display_bill(curOrder, curPrice, customer_type)
        print(bill)
        
        userInputToContinue = input("Continue for another order(Any keys= Yes, n= No)?")

        if userInputToContinue.lower() == 'n':
            print("The system is shutting down!")
            o.saveToFile(bill)
            flag = False

        