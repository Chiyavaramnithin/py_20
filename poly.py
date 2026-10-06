'''build a payment system with a base class payment(amount) and three subclass: credit card,upi,and netbanking.
each overrides a method process() with its own class logic write a function checkout(payment) that calls process()
on any payment object and demonstrate polymorphism '''

class Payment:
    def __init__(self, amount):
        self.amount = amount

    def process(self):
        raise NotImplementedError("Subclass must implement process method")

class CreditCardPayment(Payment):
    def process(self):
        print(f"Processing Credit Card payment of ₹{self.amount}")

class UPIPayment(Payment):
    def process(self):
        print(f"Processing UPI payment of ₹{self.amount}")

class NetBankingPayment(Payment):
    def process(self):
        print(f"Processing NetBanking payment of ₹{self.amount}")

def checkout(payment):
    payment.process()

payments = [
    CreditCardPayment(1000),
    UPIPayment(500),
    NetBankingPayment(2000)
]

for p in payments:
    checkout(p)

from PIL.ImImagePlugin import number


# class Bank:
#     bank_name = "ABC Bank"
#     def __init__(self,balance):
#         self.__balance = balance
#     def getbalance(self):

#         return self.__balance
#     def setbalance(self, new_balance):
#         self.__balance = new_balance
# alice = Bank(10000)
# print(alice.__balance)          --> error
# print(alice._Bank__balance)      -->access balance using name mangling
# print(alice.getbalance())
# alice.setbalance(15000)
# print(alice.getbalance())
class Bank:
    bank_name = "ABC Bank"
    def __init__(self,balance):
        self.__balance = balance
    @property
    def balance(self):
        user = input("enter username")
        pin = int(input("enter pin"))
        if user == "admin" and pin == 1111:
            return self.__balance
        else:
            return "Access Denied!!"
    # @balance.setter
    # def balance(self, new_balance):
    #     if new_balance > 0 :
    #         self.__balance = new_balance
    #     else:
    #         print("Balance cannot be less than 0!!!")
alice = Bank(10000)
# print(alice.balance)
# alice.balance = -1000

class Product:
    __profit = 1000
    def __init__(self, price):
        self.__price = price
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self.__price = new_price
product1 = Product(100)
print(product1.price)             #being able to access a private variable
                                  # like a normal variable
product1.price = 150


class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = 0
        self.balance = initial_balance

@property
def balance(self):
    return self.__balance

@balance.setter
def balance(self, value):
    if value < 0:
        raise ValueError("Balance cannot be negative")
    self.__balance = value

def deposit(self, amount):
    if amount <= 0:
        raise ValueError("Deposit amount must be positive")
    self.balance = self.__balance + amount

def withdraw(self, amount):
    if amount <= 0:
        raise ValueError("Withdraw amount must be positive")
    if amount > self.__balance:
        raise ValueError("Insufficient funds")
    self.balance = self.__balance - amount
acc = BankAccount(100)
print("Initial:", acc.balance)
acc.deposit(50)
print("After deposit:", acc.balance)
acc.withdraw(30)
print("After withdraw:", acc.balance)


import math

class Circle:
    def __init__(self, radius=1):
        self.__radius = 0
        self.radius = radius

@property
def radius(self):
    return self.__radius

@radius.setter
def radius(self, value):
    if value <= 0:
        raise ValueError("Radius must be positive")
    self.__radius = value

@property
def area(self):
    return math.pi * (self.__radius ** 2)

@property
def circumference(self):
    return 2 * math.pi * self.__radius

c = Circle(5)
print("Radius:", c.radius)
print("Area:", c.area)
print("Circumference:", c.circumference)

c.radius = 10
print("\nAfter changing radius to 10:")
print("Radius:", c.radius)
print("Area:", c.area)
print("Circumference:", c.circumference)


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

@property
def full_name(self):
    return self.first_name + " " + self.last_name

@full_name.setter
def full_name(self, name):
    parts = name.split(" ")

    self.first_name = parts[0]
    self.last_name = parts[1]


person = Person("Nithin Kumar reddy", "Chiyavaram")

print("First name:", person.first_name)
print("Last name:", person.last_name)
print("Full name:", person.full_name)

person.full_name = "Rahul Kumar"

print("\nAfter changing full name:")
print("First name:", person.first_name)
print("Last name:", person.last_name)
print("Full name:", person.full_name)