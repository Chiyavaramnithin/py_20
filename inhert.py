# # Class 1: Restaurant
# # • Create a method menu(item) that returns the price of the selected food
# # item.
# # Class 2: FoodCourt (inherits Restaurant)
# # Create the following methods:
# # • display_menu() – Display the available food items.
# # • order() – Accept the food item from the user and allow multiple orders.
# # • billing() – Display the total bill and add a packing charge of ₹20.
# # Class 3: Customer (inherits FoodCourt)
# # • Create an object of the Customer class.
# # • Call the order() method.
class Restaurant:
    def menu(self, item):
        items = {
            'burger': 200,
            'pizza' : 300,
            'coke' : 70,
            'fries' : 90
        }
        return items.get(item)
class FoodCourt(Restaurant):
    def display_menu(self):
        print("burger ->200\npizza -> 300\ncoke -> 70\nfries -> 90")
    def billing(self, total_cost):
        print("Your order total :", total_cost)
        print("Packaging charges : Rs. 20" )
        print("Your total is:", total_cost + 20)
    def order(self):
        total_cost = 0
        while True:
            self.display_menu()
            item = input("Enter your order name:")
            total_cost += self.menu(item)
            print("Do you want to order more ? y/n")
            if input() == "n":
                break
        self.billing(total_cost)
class Customer(FoodCourt):
    pass
customer1 = Customer()
customer1.order()
#from matplotlib.rcsetup import validate_whiskers


# Class 1: Cab
# • Create methods to calculate the fare for Bike, Auto, and Car rides.
# Class 2: Uber (inherits Cab)
# • Create the methods menu(), booking(), and billing().
# • Add 10% GST and apply a 15% discount if the bill is above ₹1000.
# Class 3: Ola (inherits Cab)
# • Create the methods menu(), booking(), and billing().
# • Add 12% GST and apply a 20% discount if the bill is above ₹1500.
# Driver Code
# • Ask the user to choose Uber or Ola and call the booking() method.
class Cab:
    def bike(self, distance):
        return distance * 300
    def car(self , distance):
        return distance * 500
    def auto(self, distance):
        return distance * 350

class Ola(Cab):
    def menu(self):
        print("Bike -> 300/km\nCar -> 500/km\nAuto -> 350/km ")
    def billing(self, cost):
        cost = cost + cost * 0.12
        if cost > 1500:
            cost = cost - cost * 0.2
        print("Your total fare :", cost)
    def booking(self):
        self.menu()
        vehicle = input()
        distance = int(input("Enter distance in km "))
        cost = 0
        if vehicle == 'bike':
            cost = self.bike(distance)
        elif vehicle == 'car':
            cost = self.car(distance)
        elif vehicle == 'auto':
            cost = self.auto(distance)
        self.billing(cost)
class Uber(Cab):
    def menu(self):
        print("Bike -> 300/km\nCar -> 500/km\nAuto -> 350/km ")
    def billing(self, cost):
        cost = cost + cost * 0.1
        if cost > 1000:
            cost = cost - cost * 0.15
        print("Your total fare :", cost)
    def booking(self, ):
        self.menu()
        vehicle = input()
        distance = int(input("Enter distance in km "))
        cost = 0
        if vehicle == 'bike':
            cost = self.bike(distance)
        elif vehicle == 'car':
            cost = self.car(distance)
        elif vehicle == 'auto':
            cost = self.auto(distance)
        self.billing(cost)

print("Which app do you want to open?")
choice = input()
if choice == 'uber':
    Uber().booking()
elif choice == 'ola':
    Ola().booking()
else:
    print("Invalid choice")

# Class 1: SBI
# • Create the methods deposit(amount) and check_balance().
# Class 2: UnionBank
# • Create the methods withdraw(amount) and mini_statement().
# Class 3: ATM (inherits SBI and UnionBank)
# • Create the methods menu() and transaction().
# • Allow the user to perform banking operations.
# Driver Code
# • Create an object of the ATM class.
# • Call the transaction() method.
class SBI:
    statements = []
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        SBI.statements.append("deposited - Rs. "+str(amount))
    def check_balance(self):
        print("Your available balance is Rs.", self.balance)

class UnionBank:
    def __init__(self, balance):
        self.balance = balance
    def withdraw(self, amount):
        self.balance -= amount
        SBI.statements.append("Withdrawn - Rs. "+str(amount))
    def mini_statement(self):
        print(SBI.statements)
class ATM(SBI, UnionBank):
    def __init__(self, balance):
        super().__init__(balance)
    def transaction(self):
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Mini Statement")
    def menu(self):
        while True:
            self.transaction()
            choice = input("Enter Choice:")
            if choice == '1':
                amt = int(input("Enter Amount:"))
                self.deposit(amt)
            elif choice == '2':
                amt = int(input("Enter Amount:"))
                self.withdraw(amt)
            elif choice == '3':
                self.check_balance()
            elif choice == '4':
                self.mini_statement()
            else:
                print("Invalid Choice!!")
                break
user1 = ATM(10000)
user1.menu()

