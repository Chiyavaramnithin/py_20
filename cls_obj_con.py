class A:
    pass
obj1=A()
print(type(obj1))
obj2=A()
print(id(obj1))
print(id(obj2))

class phone:
    software='android'
    count=0
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
        phone.count+=1
phone1=phone('samsung','100000')
phone2=phone('Iqoo','30000')
print(phone1.brand)
print(phone1.price)
print(phone2.brand)
print(phone2.price)
print(phone.count) # for identifing the total no of phone

'''Create a class "zomato" with attributes like class variables: discount, coupon code and a list of all the restuarant
names, instance attributes: restaurant name,a dict of items, restuarant id, calculate restuarant id based on another 
class variable restuarant number,Create a function order which takes an item_no as input and checks wheather the user
 as a entered valid item and prints final_bill,if enter coupon code correctly with discount'''

class zomato:
    discount = 30
    coupon_code = "ZOMATO30"
    restaurant_names = []
    restaurant_number = 100
    def __init__(self, restaurant_name, items):
        self.restaurant_name = restaurant_name
        self.items = items
        zomato.restaurant_number += 1
        self.restaurant_id = zomato.restaurant_number
        zomato.restaurant_names.append(restaurant_name)
    def order(self, item_no):
        if item_no in self.items:
            bill = self.items[item_no]
            coupon = input("Enter coupon code: ")
            if coupon == zomato.coupon_code:
                discount_amount = bill * zomato.discount / 100
                final_bill = bill - discount_amount
                print("Final bill:", final_bill)
            else:
                print("Invalid coupon code")
                print("Final bill:", bill)
        else:
            print("Invalid item number")
r1 = zomato("Paradise", {1: 300, 2: 280, 3: 520})
r2 = zomato("Mehfil", {1: 340, 2: 550, 3: 480})
print("Restaurant Name:", r1.restaurant_name)
print("Restaurant ID:", r1.restaurant_id)
print("Items:", r1.items)
item_no = int(input("Enter item number: "))
r1.order(item_no)

class A:
    x=20
    c=0
    def __init__(self):
        self.y=120
        self.x=40
        self.a=140
        A.c+=1
obj=A()
obj2=A()
print(obj.y)
print(obj.x)
print(obj.a)
print(obj.y)
print(obj.y)
print(obj2.c)

class A:
    def __init__(self):
        age=int(input("enter the age"))
        name=input("enter the name")
        self.age=age
        self.name=name
        if isinstance(age,int):
            print(age)
        elif isinstance(name,str):
            print(name)
        else:
            print("Invalid")
p=A()

class A:
    def __init(self):
        age=int(input("enter the age"))
        name=input("enter the name")
        self.age=age
        self.name=name
        if type(age)==int:
            print(age)
        elif type(name)==str:
            print(name)
        else:
            print("Invalid")