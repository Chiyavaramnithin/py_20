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
