''' 
SOLID Principles
- First mentioned in a paper by Rober Martin in the 00s
- SOLID stands for five principles:
    - Single Responsability: We want classes and methods to have a single responsibility. Classes and methods need to have a high cohesion and be responsible for only a single thing, which ensures that we can reuse them much easier later on.
    - Open / Closed: we want to write code that is:
        - opened for extension --> we should be able to extend existing code with new functionality
        - closed for modification --> we shouldn't need to modify the original code
    - Liskov Substitution
    - Interface Segregation
    - Dependency Inversion

Credit: The great "ArjanCodes" (https://www.youtube.com/watch?v=pTB30aXS77U)    
'''

# Example: Sales System

"""
class Order:
    items = []
    quantities = []
    prices = []
    status = "open"

    # Adds items to the order
    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    # Calculates the order's total price
    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total
    
    def set_status(self, status):
        self.status = status

class PaymentProcessor:
    # Processes debit payment
    def pay_debit(self, order, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code} for {order}")
        order.set_status("paid")
    # Processes credit payment
    def pay_credit(self, order, security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code} for {order}")
        order.set_status("paid")


---- Conclussions:
- If we want to add a new payment method (Bitcoin, Apple Pay, PayPal), we might need to modify the PaymentProcessor class so we will be violating the principle.
    - We want to define a set of classes and sub-classes so that we can define a new subclass for each new payment type.
        - We will refactor the PaymentProcessor class by adding a single abstract method and then we will create subclasses for the different PaymentProcessors types.

""" 

from abc import ABC, abstractmethod

class Order:
    items = []
    quantities = []
    prices = []
    status = "open"

    # Adds items to the order
    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    # Calculates the order's total price
    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total
    
    def set_status(self, status):
        self.status = status

class PaymentProcessor:

    @abstractmethod
    def pay(self, order, security_code):
        pass


class DebitPaymentProcessor(PaymentProcessor):

    # Processes debit payment
    def pay(self, order, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code} for {order}")
        order.set_status("paid")

class CreditPaymentProcessor(PaymentProcessor):

    # Processes credit payment
    def pay(self, order, security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code} for {order}")
        order.set_status("paid")

class PaypalPaymentProcessor(PaymentProcessor):

    # Processes credit payment
    def pay(self, order, security_code):
        print("Processing PayPal payment type")
        print(f"Verifying security code: {security_code} for {order}")
        order.set_status("paid")


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB Cable", 2, 5)

print(order.total_price())
processor = PaypalPaymentProcessor()
processor.pay(order, "0372846")


"""
- Now we won't violate the second principle anymore, because if you want to add another payment method, we don't have to change any of the main classes anymore (Order, PaymentProcessor)
"""
