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
