''' 
SOLID Principles
- First mentioned in a paper by Rober Martin in the 00s
- SOLID stands for five principles:
    - Single Responsability: We want classes and methods to have a single responsibility. Classes and methods need to have a high cohesion and be responsible for only a single thing, which ensures that we can reuse them much easier later on.
    - Open / Closed: we want to write code that is:
        - opened for extension --> we should be able to extend existing code with new functionality
        - closed for modification --> we shouldn't need to modify the original code
    - Liskov Substitution: if you have objects in a programme, you should be able to replace those objects with instances of their subtypes or subclasses without altering the correctness of the programme.
    - Interface Segregation
    - Dependency Inversion

Credit: The great "ArjanCodes" (https://www.youtube.com/watch?v=pTB30aXS77U)    
'''

# Example: Sales System

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

---- Conclussions:
- If we the PaypalPaymentProcessor did not work with security codes and required email addresses instead, we would be violating the Liskov Substitution principle, because the pay method in the PaymentProcessor Abstract Class would be doing something different than supposed to.
    - One way to solve this, is removing this dependency from the payment method in from the pay method and set it in the initializer.
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
    def pay(self, order):
        pass


class DebitPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code

    # Processes debit payment
    def pay(self, order):
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code} for {order}")
        order.set_status("paid")

class CreditPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code

    # Processes credit payment
    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code} for {order}")
        order.set_status("paid")

class PaypalPaymentProcessor(PaymentProcessor):

    def __init__(self, email_address):
        self.email_address = email_address

    # Processes credit payment
    def pay(self, order):
        print("Processing PayPal payment type")
        print(f"Verifying email address: {self.email_address} for {order}")
        order.set_status("paid")


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB Cable", 2, 5)

print(order.total_price())
processor = PaypalPaymentProcessor("test@test.com")
processor.pay(order)

"""
- Now we won't violate the second principle anymore, because if you want to add another payment method, we don't have to change any of the main classes anymore (Order, PaymentProcessor)
"""
