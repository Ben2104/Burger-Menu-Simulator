from Order import *

orderDict = {
    1: 2,
    3: 4,
    5: 6
}

o = Order()

def testCalcPrice(order):
    assert o.calculatePrice(order) == 70, "should be 12 total"
    print("Test passed, calculatePrice works")

testCalcPrice(orderDict)