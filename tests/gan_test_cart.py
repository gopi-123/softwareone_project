import sys
sys.path.append(r"C:\Users\Gopi\Documents\Python Scripts\swo_python_exercise\test-shoppingcart")

from shoppingcart.cart_copy import ShoppingCart
#import locale
#locale.setlocale(locale.LC_ALL, 'nl_NL')

def test_add_item():
    cart = ShoppingCart()
    cart.add_item("apple", 1)
    
    cart.add_item("kiwi", 1)
    #cart.add_item("apple", 15)
    cart.add_item("canberry", 15)

    receipt = cart.print_receipt()
    print(receipt)
    print(cart._get_product_price("orange1"))
    print(cart.currency("hi_IN"))

    assert receipt[0] == "apple - 1 - € 1,00"


def test_add_item_with_multiple_quantity():
    cart = ShoppingCart()
    cart.add_item("apple", 2)

    receipt = cart.print_receipt()
    print(receipt)

    assert receipt[0] == "apple - 2 - € 2,00"


def test_add_different_items():
    cart = ShoppingCart()
    cart.add_item("banana", 1)
    cart.add_item("kiwi", 1)
    

    receipt = cart.print_receipt()

    assert receipt[0] == "banana - 1 - € 1,10"
    assert receipt[1] == "kiwi - 1 - € 3,00"

test_add_item()
test_add_item_with_multiple_quantity()
test_add_different_items()
