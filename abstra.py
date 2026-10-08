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

'''Design an abstract class PaymentGateway using ABC with abstract methods initiate(amount), verify(transaction_id), 
and refund(transaction_id). Create two concrete classes RazorpayGateway and PayPalGateway that inherit from
PaymentGateway and implement all three methods. Create objects of both concrete classes and call their methods. Also
verify that PaymentGateway cannot be instantiated directly.'''

from abc import ABC, abstractmethod
class paymentgateway(ABC):
    @abstractmethod
    def initiate(self,amount):
        pass
    @abstractmethod
    def verify(self,transaction_id):
        pass
    @abstractmethod
    def refund(self,transaction_id):
        pass
class razorpay(paymentgateway):
    def initiate(self,amount):
        print("razorpay initiate",amount)
    def verify(self,transaction_id):
        print("razorgateway verified",transaction_id)
    def refund(self,transaction_id):
        print("razorgateway refund",transaction_id)
class paypalgateway(paymentgateway):
    def initiate(self,amount):
        print("paypalgateway initiate",amount)
    def verify(self,transaction_id):
        print("paypalgateway verified",transaction_id)
    def refund(self,transaction_id):
        print("paypalgateway refund",transaction_id)
p=razorpay()
p.initiate(900)
p.verify(800)
p.refund(700)

s=paypalgateway()
s.initiate(90)
s.verify(80)
s.refund(70)

'''Create an abstract class Animal(ABC) with abstract methods speak() and move(), and a concrete method breathe()
shared by all. Implement Dog, Bird, and Fish. Prove that the contract is enforced by trying to instantiate Animal
or a subclass that forgot to implement speak().'''
from abc import ABC,abstractmethod
class animal(ABC):
    @abstractmethod
    def speak(self):
        pass
    def move(self):
        pass
    def breathe(self):
        pass
class dog(animal):
    def speak(self):
        print("dog say woof")
    def move(self):
        print("dog can run with 4 legs")
    def breathe(self):
        print("dog can breathe")
class bird(animal):
    def speak(self):
        print("brid say chirp")
    def move(self):
        print("bird cn fly with feathers")
    def breathe(self):
        print("bird can breathe")
class fish(animal):
    def speak(self):
        print("fish says blub")
    def move(self):
        print("fish is used to swim")
    def breathe(self):
        print("fish can breathe")
a=dog()
a.speak()
a.move()
a.breathe()
b=bird()
b.speak()
b.move()
b.breathe()
c=fish()
c.speak()
c.move()
c.breathe()

'''Create an abstract class DataStorage(ABC) with an abstract property storage_type and abstract methods save(data), 
load(key), and delete(key). Implement FileStorage and MemoryStorage. Demonstrate that both are interchangeable.'''

from abc import ABC,abstractmethod
class datastorage(ABC):
    @property
    @abstractmethod
    def storage_type(self):
        pass
    @abstractmethod
    def save(self,data):
        pass
    @abstractmethod
    def load(self,key):
        pass
    def delete(self,key):
        pass
class filestorage(datastorage):
    @property
    def storage_type(self):
        return " file storage"
    def save(self,data):
        print("saving the data",data)
    def load(self,key):
        print("loading data from file",key)
    def delete(self,key):
        print("delete the data from file",key)
class memorystorage(datastorage):
    @property
    def storage_type(self):
        return " memory storage"
    def save(self,data):
        print("save the date from file",data)
    def load(self,key):
        print("load the data from file",key)
    def delete(self,key):
        print("delete the data from file",key)
f=filestorage()
print(f.storage_type)
f.save("hello")
f.load(20)
f.delete(10)
m=memorystorage()
print(m.storage_type)
m.save("King")
m.load(200)
m.delete(100)