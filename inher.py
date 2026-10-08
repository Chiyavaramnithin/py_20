l = [1,2,3,4,5]
for i in l:
    print(i)

it = iter(l)
it = l.__iter__()
print(it)

print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())

class A:
    def __init__(self):
        self.val = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.val <= 5:
            num = self.val
            self.val += 1
            return num
        else:
            raise StopIteration

obj = A()
for i in obj:
    print(i)

print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
obj2 = A()
print(obj2.__next__())
print(next(obj2))
l = list(range(1, 11))
print(l)
class Numbers:
    def __init__(self, start, end):
        self.val = start
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.val <= self.end:
            current = self.val
            self.val += 1
            return current
        else:
            raise StopIteration
five_to_ten = Numbers(5, 10)
# for i in five_to_ten:
#     print(i)

twenty_to_hundred = Numbers(20, 100)
# for i in twenty_to_hundred:
#     print(i)

class Fibonacci:
    def ddddddd__init__(self, n):
        self.count = 1
        self.n = n
        self.a , self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count <= self.n:
            val = self.a
            self.a, self.b = self.b, self.a + self.b
            self.count += 1
            return val
        else:
            raise StopIteration
five = Fibonacci(5)
# for i in five:
#     print(i)
#
ten = Fibonacci(10)
for i in ten:
    print(i)
class A:
    c1 = "hey"
    c2 = 123
    def __init__(self, x, y):
        self.x = x
        self.y = y
class B(A):
    c3 = True
    def __init__(self, z, x, y):
        self.z = z
        # A.__init__(self,x, y)
        super().__init__(x, y)
b = B(10, 20, 30)
print(b.c1)
print(b.c2)
print(b.c3)
print("z :",b.z)
print("x :",b.x)
print("y :",b.y)
class A:
    def __init__(self, x):
        self.x = x
class B(A):
    def __init__(self, x , y):
        self.y = y
        A.__init__(self, x)
        super().__init__(x)
class C(B):
    def __init__(self, x, y , z):
        self.z = z
         B.__init__(self, x, y)
        super().__init__(x, y)
c = C(10, 20 , 30)
print("x: ",c.x)
print("y :",c.y)
print("z :" ,c.z)
# Create a Bank class with:
# • balance variable
# • deposit()
# • withdraw()
# • check_balance()
# Create a User class that inherits Bank and displays the user's name. Perform
# deposit, withdrawal, and balance check.

class Bank:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Dear {self.name},\nYour account has been credited with Rs.{amount} successfully.")
    def withdraw(self, amount):
        self.balance -= amount
        print(f"Dear {self.name},\nYour account has been debited with Rs.{amount} successfully.")
    def check_balance(self):
        print(f"Dear {self.name},\nYour current available balance is Rs.{self.balance}.")

class User(Bank):
    def __init__(self, name, balance):
        self.name = name
#         super().__init__(balance)
# user1 = User("John", 10000)
# user2 = User("Alice", 120000)
# print(user1.__dict__)
# print(user2.__dict__)
# print(user1.name)
# print(user2.name)
# user1.deposit(5000)
# user1.check_balance()
# user2.withdraw(2000)
# user2.deposit(10000)
# user2.check_balance()

# Create an Employee class with:
# • emp_name
# • salary
# • display_details()
# Create a Manager class that inherits Employee and adds a bonus(). Display the
# total salary.
class Employee:
    def __init__(self, emp_name, salary):
        self.emp_name = emp_name
        self.salary = salary
    def display_details(self):
        print(f"Employee Name: {self.emp_name}, Salary: {self.salary}")

class Manager(Employee):
    def bonus(self):
        self.salary += self.salary * 0.1
# alice = Manager("Alice", 15000)
# alice.display_details()
# alice.bonus()
# alice.display_details()


class A:
    def __init__(self):
        self.x = 10
        self.y = 20
        self.z = 30
        self.count = 40
    def check_even(self, val):
        if val % 2 == 0:
            print("Even")
        else:
            print("Odd")
class B:
    def __init__(self, count):
        self.count = count
    def m1(self):
        obj = A()
        obj.check_even(self.count)
b = B(100)
print(b.count)
b.m1()
print(b.count)