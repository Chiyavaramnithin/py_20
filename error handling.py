# Create a class Person whose constructor takes age as an argument. Raise a ValueError if the age is less than 0.

class person:
    def __init__(self,age:int=0):
        if age<=0:
            raise ValueError("Age should be greater than 0")
        self.age=age
p1=input()
p=person(int(p1))
print(p.age)

