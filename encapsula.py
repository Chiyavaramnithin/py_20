#Encapsulation Questions

class Bank:
    def __init__(self, balance):
        self.__balance = balance
    @property
    def balance(self):
        pin = int(input("Enter Pin:"))
        if pin == 1234:
            return self.__balance
        else:
            return "Access Denied"

    @balance.setter
    def balance(self, new_balance):
        if new_balance <= 0:
            raise ValueError("Invalid Balance")
        else:
            self.__balance = new_balance
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        self.__balance -= amount
b1 = Bank(100000)
print(b1.balance)
b1.balance = 2000
print(b1.balance)
b1.balance = -100
b1.deposit(1000)
print(b1.balance)
b1.withdraw(1500)
print(b1.balance)


#Q2
import math
class Circle:
    def __init__(self, radius):
        self.__radius = radius
    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self, radius):
        if radius > 0:
            self.__radius = radius
    @property
    def area(self):
        return math.pi * self.__radius ** 2
    @property
    def circumference(self):
        return 2 * math.pi * self.__radius
c1 = Circle(5)
print(c1.radius)
print(c1.area)
print(c1.circumference)


#Q3
class Config:
    def __init__(self):
        self.system_name = "SYS"
        self._settings = {'theme': 'dark',
                          'RAM' : 4,
                          'ROM': 12 }
        self.__secret_key = "PY20"
    def get_settings(self, key):
        return self._settings[key]
c1 = Config()
print(c1.system_name)
print(c1._settings)   #use w caution settings is protected.
print(c1._Config__secret_key)
print(c1.get_settings("RAM"))


#Q4
class Person:
    def __init__(self, first_name , last_name):
        self.__first_name = first_name
        self.__last_name = last_name
    @property
    def first_name(self):
        return self.__first_name
    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name
    @property
    def last_name(self):
        return self.__last_name
    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name
    @property
    def full_name(self):
        return self.first_name+" "+self.last_name
    @full_name.setter
    def full_name(self, full_name):
        self.__full_name = full_name
        self.first_name , self.last_name = full_name.split(" ")
person1 = Person("Alice", "Smith")
print(person1.first_name)
print(person1.last_name)
print(person1.full_name)
person1.first_name = "John"
print(person1.first_name)
print(person1.full_name)
person1.full_name = "Jane Doe"
print(person1.first_name)
print(person1.last_name)
print(person1.full_name)

from abc import ABC, abstractmethod

class Whatsapp(ABC):
    @abstractmethod
    def send(self):
        pass

class SendPhoto(Whatsapp):
    def send(self):
        print("Compressing the photo...")
        print("Encrypting Photo...")
        print("Sending the photo...")
        print("Decrypting the photo...")
        print("Photo sent!")

class SendText(Whatsapp):
    def send(self):
        print("Checking character limit..")
        print("Encrypting the message...")
        print("Sending the message..")
        print("Decrypting the message...")
        print("Message sent!!")

message1 = SendText()
image1 = SendPhoto()
message1.send()
image1.send()