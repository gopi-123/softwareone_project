import typing

from . import abc
from collections import OrderedDict
import json
import locale
import os


#Refactor intermediate variables
#len (cart) --https://youtu.be/HheLDNNEX4s

class ShoppingCart(abc.ShoppingCart):
    def __init__(self):
        self._items =  OrderedDict() 
        self.currency_code = "nl_NL"
        self.json_file_path = "product_price.json"

    def add_item(self, product_code: str, quantity: int):
        if product_code not in self._items:
            self._items[product_code] = quantity
        else:
            self._items[product_code] += quantity

    def print_receipt(self) -> typing.List[str]:
        lines = []
        total_price = 0.00 
        locale.setlocale(locale.LC_ALL, self.currency_code)
        
        #Can use lst compreshension to use lists or for loop

        for item in self._items.items():
            
            price = self._get_product_price(item[0]) * item[1]         

            lines.append(item[0] + ' - ' + str(item[1]) + ' - ' + locale.currency(price))
            
            total_price += price 

        
        lines.append('Total = ' + locale.currency(total_price))
        
        return lines

    def _get_product_price(self, product_code: str) -> float:      
        
        try:
            self.json_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), self.json_file_path)
            
            print("json path", self.json_file_path)
            with open(self.json_file_path, 'r') as json_file:
                json_price_data = json.load(json_file)
                return json_price_data.get(product_code, 0.0)
        
        except FileNotFoundError:
            raise Exception("FileNotFoundError")
            #raise Exception("Sorry file {} does not exist".format(self.json_file_path))
            #print("Sorry file {} does not exist".format(self.json_file_path))
    
        
