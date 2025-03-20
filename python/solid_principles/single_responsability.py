''' 
SOLID Principles
- First mentioned in a paper by Rober Martin in the 00s
- SOLID stands for five principles:
    - Single Responsability: We want classes and methods to have a single responsibility. Classes and methods need to have a high cohesion and be responsible for only a single thing, which ensures that we can reuse them much easier later on.
    - Open / Closed
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
    
    # Processes the payment
    def pay(self, payment_type, security_code):
        if payment_type == "debit":
            print("Processing debit payment type")
            print(f"Verifying security code: {security_code}")
            self.status = "paid"
        elif payment_type == "credit":
            print("Processing credit payment type")
            print(f"Verifying security code: {security_code}")
            self.status = "paid"
        else: 
            raise Exception(f"Unknown payment type: {payment_type}")

    order = Order()
    order.add_item("Keyboard", 1, 50)
    order.add_item("SSD", 1, 150)
    order.add_item("USB Cable", 2, 5)

    print(order.total_price())
    order.pay("debit", "0372846")

---- Conclussions:
- The class Order does many things: adds items to the order, calculates the order's total price and processes the payment.
- Payment processing shouldn't be part of the Order class. 
    - We will fix this in the following  lines by inserting the 'pay' method in another class.
        -  This will be benefecial becuase we can add other payment methods without modifying the 'Order' class
- 'pay' method's 'if' clause is not ideal becuase it checks for different payment types
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

class PaymentProcessor:
    # Processes the payment
    def pay(self, payment_type, security_code):
        if payment_type == "debit":
            print("Processing debit payment type")
            print(f"Verifying security code: {security_code}")
            self.status = "paid"
        elif payment_type == "credit":
            print("Processing credit payment type")
            print(f"Verifying security code: {security_code}")
            self.status = "paid"
        else: 
            raise Exception(f"Unknown payment type: {payment_type}")
