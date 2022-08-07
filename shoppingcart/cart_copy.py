import typing

from . import abc
from collections import OrderedDict
import json
import locale

json_file_path = r"C:\Users\Gopi\Documents\Python Scripts\swo_python_exercise\test-shoppingcart\shoppingcart\product_price.json"
#Refactor intermediate variables
#len (cart) --https://youtu.be/HheLDNNEX4s

class ShoppingCart(abc.ShoppingCart):
    def __init__(self):
        self._items =  dict() #OrderedDict() #
        #Python’s OrderedDict is a dict subclass that preserves the order in which key-value pairs, 
        # commonly known as items, are inserted into the dictionary.

    def add_item(self, product_code: str, quantity: int):
        if product_code not in self._items:
            self._items[product_code] = quantity
        else:
            #q = self._items[product_code]
            #self._items[product_code] = q + quantity
            self._items[product_code] += quantity

    def print_receipt(self) -> typing.List[str]:
        lines = []
        total_price = 0.00 
        locale.setlocale(locale.LC_ALL, 'nl_NL')

        
        #Can use lst compreshension to use lists or for loop

        for item in self._items.items():
            price = self._get_product_price(item[0]) * item[1]

            print(price)

            #price_string = "€%.2f" % price
            #locale.currency(price)
            #locale.currency(price,grouping = True)

            lines.append(item[0] + ' - ' + str(item[1]) + ' - ' + locale.currency(price))
            #lines.append(item[0] + ' - ' + str(item[1]) + ' - ' + '€%.2f' % price)

            #total_price += self._get_product_price(item[0]) * item[1]
            total_price += price 

        #format(price,'.2f')
        lines.append('Total = ' + locale.currency(total_price))#lines[-1] gives sum of final
        #lines.append('Total = ' + '€%.2f' % total_price) #lines[-1] gives sum of final
        
        return lines

    def _get_product_price(self, product_code: str) -> float: 
               
        product_price = {
            'apple' : 1.0,
            'banana' : 1.1,
            'kiwi' : 3.0
        }
        
        if product_code in product_price:
            return product_price.get(product_code, 0.0)
        else:
            try:
                with open(json_file_path, 'r') as json_file:
                    json_price_data = json.load(json_file)
                    return json_price_data.get(product_code, 0.0)
            except FileNotFoundError:
                print(f"Sorry file{json_file_path} does not exist")
        

    """
    def total(self):
        total_out = sum(self.price_list)
    """

    def currency(self, currency_type_lang_code):
        prodprice = 0.00
        
        import locale
        locale.setlocale(locale.LC_ALL, '')   # use user's preferred locale
        #locale.setlocale(locale.LC_ALL, currency_type_lang_code) #use German locale
        # return '{}: {}'.format(lang_name, currency)
        return locale.currency( prodprice,grouping=True )
        


        
        
        
