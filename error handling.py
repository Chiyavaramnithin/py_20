# Create a class Person whose constructor takes age as an argument. Raise a ValueError if the age is less than 0.

class person:
    def __init__(self,age:int=0):
        if age<=0:
            raise ValueError("Age should be greater than 0")
        self.age=age
p1=input()
p=person(int(p1))
print(p.age)

#Create a class Student with an attribute marks. Implement a method set_marks(marks) that raises a ValueError if
# marks are not in the range 0 to 100.

class Student:
    def __init__(self,marks=int):
        if marks<0 or marks>100:
            raise ValueError("marks are not in the range 0 to 100")
        self.marks=marks
p=input()
p1=Student(int(p))
print(p1.marks)