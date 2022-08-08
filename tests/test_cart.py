import sys
sys.path.append(r"C:\Users\Gopi\Documents\Python Scripts\softwareone_project")

import unittest 
from shoppingcart.cart import ShoppingCart

class TestShoppingCart(unittest.TestCase):

    def test_add_item(self):
        cart = ShoppingCart()
        cart.add_item("apple", 1)

        receipt = cart.print_receipt()
        
        assert receipt[0] == "apple - 1 - € 1,00"


    def test_add_item_with_multiple_quantity(self):
        cart = ShoppingCart()
        cart.add_item("apple", 2)
        cart.add_item("apple", 3)

        receipt = cart.print_receipt()  

        assert receipt[0] == "apple - 5 - € 5,00"


    def test_add_different_items(self):
        cart = ShoppingCart()
        cart.add_item("banana", 1)
        cart.add_item("kiwi", 1)    

        receipt = cart.print_receipt()

        assert receipt[0] == "banana - 1 - € 1,10"
        assert receipt[1] == "kiwi - 1 - € 3,00"

    def test_different_currency(self):        
        #Test currency for US Dollars
        cart = ShoppingCart()
        cart.currency_code = "en_US"

        cart.add_item("apple", 1)

        receipt = cart.print_receipt()
  
        assert receipt[0] == "apple - 1 - $1.00"
        
        #Test currency for British Pounds
        cart2 = ShoppingCart()
        cart2.currency_code = "en_GB"

        cart2.add_item("apple", 1)
        receipt = cart2.print_receipt()

        assert receipt[0] == "apple - 1 - £1.00"

    def test_total_price(self):
        cart = ShoppingCart()
        cart.add_item("apple", 1)
        cart.add_item("kiwi", 2)
        
        receipt = cart.print_receipt()

        assert receipt[-1] == "Total = € 7,00"

    def test_print_receipt(self):
        cart = ShoppingCart()
        cart.add_item("apple", 1)
        cart.add_item("kiwi", 2)
        
        receipt = cart.print_receipt()

        assert receipt == ['apple - 1 - € 1,00', 'kiwi - 2 - € 6,00', 'Total = € 7,00']

if  __name__ == '__main__': 
    unittest.main()
