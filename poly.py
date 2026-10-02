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
