import typing
from . import abc
from collections import OrderedDict
import json
import locale
import os

class ShoppingCart(abc.ShoppingCart):
    """
    A Class used to implement Shopping Cart System
    """

    def __init__(self):
        self._items =  OrderedDict() 

        #display the product prices in different currencies
        self.currency_code = "nl_NL"
        self.json_file_path = "product_price.json"

    def add_item(self, product_code: str, quantity: int):
        """
        Function to add products into shopping cart
        It takes parameters such as product_code and quantity of product
        """

        if product_code not in self._items:
            self._items[product_code] = quantity
        else:
            self._items[product_code] += quantity

    def print_receipt(self) -> typing.List[str]:
        """
        Function to print shopping receipt having the list of product code
        quantity and price. It returns list of strings as output
        """

        lines = []
        total_price = 0.00 
        #display the product prices in required currency code
        locale.setlocale(locale.LC_ALL, self.currency_code)

        for item in self._items.items():
            
            price = self._get_product_price(item[0]) * item[1]         

            lines.append(item[0] + ' - ' + str(item[1]) + ' - ' + locale.currency(price))
            
            total_price += price 

        #Add total line to the receipt
        lines.append('Total = ' + locale.currency(total_price))
        
        return lines

    def _get_product_price(self, product_code: str) -> float:  
        """
        Function to extract price for the given product code as parameter
        and returns the price in float format. 
        """    
        
        try:
            #fetch product prices from json file
            self.json_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), self.json_file_path)
            with open(self.json_file_path, 'r') as json_file:
                json_price_data = json.load(json_file)
                return json_price_data.get(product_code, 0.0)
        
        except FileNotFoundError:
            raise Exception("Sorry file {} does not exist".format(self.json_file_path))
    
        