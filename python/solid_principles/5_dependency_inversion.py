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
    - Dependency Inversion: we want our classes to depend on abstractions and not on concrete subclasses.

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

class SMSAuthenticator:

    authorized = True

    # Verifying auth code
    def verify_code(self, code):
        print(f"Verifying code {code}")
        self.authorized = True

    # Checking the authorized state
    def is_authorized(self) -> bool:
        return self.authorized

# General Purpose Interface
class PaymentProcessor:

    @abstractmethod
    def pay(self, order):
        pass

class DebitPaymentProcessor(PaymentProcessor):

    def __init__(self, authorizer: SMSAuthenticator, security_code):
        self.authorizer = authorizer
        self.security_code = security_code

    # Processes debit payment
    def pay(self, order):
        if not self.authorizer.is_authorized():
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

class PaypalPaymentProcessor(PaymentProcessor):

    def __init__(self, authorizer: SMSAuthenticator, email_address):
        self.authorizer = authorizer
        self.email_address = email_address

    # Processes credit payment
    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not Authorized")
        print("Processing PayPal payment type")
        print(f"Verifying email address: {self.email_address} for {order}")
        order.set_status("paid")

---- Conclussions:
- Payment processes are dependin on specific authorizers. To fix this we will create a new Abstract class so that the Debit and Paypal processors do not depend on the SMSAuthenticator class.

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

class Authorizer:
    
    @abstractmethod
    def is_authorized(self) -> bool:
        pass

class SMSAuthenticator(Authorizer):

    authorized = True

    # Verifying auth code
    def verify_code(self, code):
        print(f"Verifying code {code}")
        self.authorized = True

    # Checking the authorized state
    def is_authorized(self) -> bool:
        return self.authorized
    
class NotARobotAuth(Authorizer):
    
    authorized = True

    # Verifying if robot
    def not_a_robot(self):
        print("Are you a robot? Nope")
        self.authorized = True

    # Checking the authorized state
    def is_authorized(self) -> bool:
        return self.authorized


# General Purpose Interface
class PaymentProcessor:

    @abstractmethod
    def pay(self, order):
        pass

class DebitPaymentProcessor(PaymentProcessor):

    def __init__(self, authorizer: Authorizer, security_code):
        self.authorizer = authorizer
        self.security_code = security_code

    # Processes debit payment
    def pay(self, order):
        if not self.authorizer.is_authorized():
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

class PaypalPaymentProcessor(PaymentProcessor):

    def __init__(self, authorizer: Authorizer, email_address):
        self.authorizer = authorizer
        self.email_address = email_address

    # Processes credit payment
    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not Authorized")
        print("Processing PayPal payment type")
        print(f"Verifying email address: {self.email_address} for {order}")
        order.set_status("paid")


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB Cable", 2, 5)

print(order.total_price())
authorizer = NotARobotAuth() 
processor = PaypalPaymentProcessor(authorizer, "test@test.com")
# processor.pay(order)   -- Exception: Not Authorized
authorizer.not_a_robot()
processor.pay(order)

"""
- Now we won't violate the second principle anymore, because if you want to add another payment method, we don't have to change any of the main classes anymore (Order, PaymentProcessor)
"""
