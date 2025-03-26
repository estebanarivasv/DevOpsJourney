''' 
SOLID Principles
- First mentioned in a paper by Rober Martin in the 00s
- SOLID stands for five principles:
    - Single Responsability: We want classes and methods to have a single responsibility. Classes and methods need to have a high cohesion and be responsible for only a single thing, which ensures that we can reuse them much easier later on.
    - Open / Closed: we want to write code that is:
        - opened for extension --> we should be able to extend existing code with new functionality
        - closed for modification --> we shouldn't need to modify the original code
    - Liskov Substitution: if you have objects in a programme, you should be able to replace those objects with instances of their subtypes or subclasses without altering the correctness of the programme.
    - Interface Segregation: overall, it is better if we have several specific purpose interfaces instead of one big general purpose interface.
        - Inheiratence tree: Create a hierarchical structure of classes
            - Hard to understand && cause unwanted side effects if base class is changes
        - Composition: creates objects that contains objects as parts
            - Complex structures into simpler ones && accommodate future requirement changes more easily.
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

---- Conclussions:
- Inheritatence tree (4_1): If we want to start having an authentication step via sms in the payment method for all the many payment types but not all of them started accepting this, we might do something like:
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

# General Purpose Interface
class PaymentProcessor:

    @abstractmethod
    def pay(self, order):
        pass

# Specific Purpose Interface
class PaymentProcessor_SMS(PaymentProcessor):

    @abstractmethod
    def auth_sms(self, code):
        pass


class DebitPaymentProcessor(PaymentProcessor_SMS):

    def __init__(self, security_code):
        self.security_code = security_code
        self.verified = False

    def auth_sms(self, code):
        print(f"Verifying SMS code {code}")
        self.verified = True

    # Processes debit payment
    def pay(self, order):
        if not self.verified:
            raise Exception("Not Authorized")
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

class PaypalPaymentProcessor(PaymentProcessor_SMS):

    def __init__(self, email_address):
        self.email_address = email_address
        self.verified = False

    def auth_sms(self, code):
        print(f"Verifying SMS code {code}")
        self.verified = True

    # Processes credit payment
    def pay(self, order):
        if not self.verified:
            raise Exception("Not Authorized")
        print("Processing PayPal payment type")
        print(f"Verifying email address: {self.email_address} for {order}")
        order.set_status("paid")


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB Cable", 2, 5)

print(order.total_price())
processor = PaypalPaymentProcessor("test@test.com")
# processor.pay(order)   -- Exception: Not Authorized
processor.auth_sms("test")
processor.pay(order)
