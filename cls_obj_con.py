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

'''Create a class "zomato" with attributes like class variables: discount, coupon code and a list of all the restuarant
names, instance attributes: restaurant name,a dict of items, restuarant id, calculate restuarant id based on another 
class variable restuarant number,Create a function order which takes an item_no as input and checks wheather the user
 as a entered valid item and prints final_bill,if enter coupon code correctly with discount'''


class Zomato:
    restaurant_names = []
    restaurant_no = 0
    coupon_code = "PY20"
    discount = 0.2
    def __init__(self, restaurant_name , restaurant_menu):
        Zomato.restaurant_no += 1
        self.restaurant_name = restaurant_name
        self.restaurant_id = Zomato.restaurant_no
        self.restaurant_menu = restaurant_menu
        Zomato.restaurant_names.append(restaurant_name)
Paradise = Zomato("Paradise",
                  {"Chicken Biryani" : 200,
                   "Mutton Biryani" : 300,
                   "Coke" : 40})
Pista_House= Zomato("Pista House",
                  {"Chicken Biryani" : 250,
                   "Mutton Biryani" : 290,
                   "Apricot Delight" : 200})
KFC = Zomato("KFC",
                  {"Chicken Burger" : 200,
                   "Chicken Wings" : 350,
                   "Coke" : 40,
                   "Fries" : 70})
def order(item_no, restaurant):
    order_items = list(restaurant.restaurant_menu.items())
    cost = order_items[item_no - 1][1]
    print("Your Cart Value is :Rs.", cost)
    print("Do you have a coupon code ?")
    cc = input("Y / N ?")
    if cc == 'Y':
        code = input("Enter the Coupon Code :")
        if code == Zomato.coupon_code:
            cost = cost - cost * Zomato.discount
        else :
            print("Invalid Coupon Code.")
    print("Your Final Bill is :Rs.", cost)
c = 0
for i in Zomato.restaurant_names:
    c += 1
    print(c ,":", i)
choice = int(input("Enter the Restaurant Number :"))
if choice == 1:
    c = 0
    for i in Paradise.restaurant_menu.items():
        c += 1
        print(c, ":", i)
    item_no = int(input("Enter Your Item Number"))
    order(item_no, Paradise)
elif choice == 2:
    c = 0
    for i in Pista_House.restaurant_menu.items():
        c += 1
        print(c, ":", i)
    item_no = int(input("Enter Your Item Number"))
    order(item_no, Pista_House)
elif choice == 3:
    c = 0
    for i in KFC.restaurant_menu.items():
        c += 1
        print(c, ":", i)
    item_no = int(input("Enter Your Item Number"))
    order(item_no, KFC)
else:
    print("Invalid Input")




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
p=A()


