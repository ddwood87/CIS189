"""
Student: Dominic Wood
Class: CIS189
CRN: 21906
Module: 10
Topic: 2
Assignment: Invoice Class
Date: 03/23/2023
"""
from Customer import Customer
from json import dumps

class Invoice:
    _invoice_id: int
    _customer: Customer
    _items_with_price: dict[str, float]

    #Cannot have more than one __init__ method.
    #Simulate polymorphism with optional args.
    def build(self, invoice_id: int, customer: Customer, items_with_price=...):
        self._invoice_id = invoice_id
        self._customer = customer
        if isinstance(items_with_price, dict):
            self._items_with_price = items_with_price
        else:
            self._items_with_price = dict()
    
    #Constructor accepts customer fields, or customer object.
    #Navigates proper method.
    def __init__(self, 
                 invoice_id: int,
                 cust_id: int=..., 
                 address: str=..., 
                 last_name: str=..., 
                 first_name: str=..., 
                 phone_number: str=...,
                 items_with_price: dict=...,
                 *, customer: Customer=None):
        if customer == None:
            #check that required parameters are given
            if (cust_id != ... 
                    and address != ... 
                    and last_name != ...
                    and first_name != ...
                    and phone_number != ...):
                cust = Customer(cust_id, last_name, first_name, phone_number, address)
            else:
                raise ValueError("Not enough customer info given.")
        else:
            cust = customer
        if items_with_price == None:
            self.build(invoice_id, cust)
        else:
            self.build(invoice_id, cust, items_with_price)

    def __str__(self) -> str:
        result = f'\nInvoice Id: {self._invoice_id}\n'
        result += str(self._customer) + '\n'
        price_total = 0
        if len(self._items_with_price) > 0:
            result += "Items:\n"
            for key in self._items_with_price:
                item_name = key
                item_price = self._items_with_price[key]
                
                result += f'{item_name:>10}: ${item_price:>8.2f}\n'
        else:
            result += 'No items invoiced.\n'
        return result

    def __repr__(self) -> str: 
        json_object = dumps(self)
        return json_object
    
    def add_item(self, item: dict[str, float]):
        self._items_with_price.update(item)
    
    def create_invoice(self):
        price_total = 0
        tax_rate = .06
        for key in self._items_with_price:
            price_total += self._items_with_price[key]
        print(str(self))
        print(f'{"Subtotal":<10}:  {price_total:>8.2f}')
        tax_total = price_total * tax_rate
        print(f'{"Tax":<10}:  {tax_total:>8.2f}')
        total = price_total + tax_total
        print(f'{"Total":<10}: ${total:>8.2f}')

if __name__ == '__main__':
    # Driver code
    # Customer info parameters given.
    try:
        invoice = Invoice(1, 123, '1313 Disneyland Dr, Anaheim, CA 92802' ,'Mouse', 'Minnie', '555-867-5309')
        invoice.add_item({'iPad': 799.99})
        invoice.add_item({'Surface': 999.99})
        invoice.create_invoice()
    except ValueError as err:
        print(err)

    # Customer object parameter given.
    try:
        cust = Customer(321, 'Duck', 'Daffy', '555-333-7777', '2324 Pond Drive')
        items = {'iPad': 799.99, 'Surface': 999.99}
        invoice2 = Invoice(2, customer=cust, items_with_price=items)
        invoice2.create_invoice()
    except ValueError as err:
        print(err)