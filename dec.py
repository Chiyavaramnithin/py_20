'''Decorators Questions
1. Create functions add(a, b), subtract(a, b) and multiply(a, b).
Create a function calculate(operation, a, b) that accepts a function reference and performs the selected operation.
Use lambda functions to perform:
* Square of a number
* Cube of a number
* Double of a number
Add a decorator log_operation that prints "Operation started" before execution and "Operation completed" after execution.'''

def log_operation(func):
    def wrapper(*args,**kwargs):
        print("Operation started")
        result=func(*args,**kwargs)
        print("Operation completed")
        return result
    return wrapper
@log_operation
def calculate(operation,a,b):
    return operation(a,b)
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
print(calculate(add,5,6))
print(calculate(sub,5,6))
print(calculate(mul,5,6))
square=lambda x:x**2
cube=lambda x:x**3
double=lambda x:x*2

print(square(7))
print(cube(7))
print(double(7))

''' . Create a function process_marks(marks, operation) where operation is a function reference.

Use lambda functions to:

* Add 5 grace marks
* Double each mark
* Find whether a mark is greater than 40

Create a decorator that prints "Processing started" and "Processing completed".'''

def ad(func):
    def wrapper(*args,**kwargs):
        print("Processing Started")
        result=func(*args,**kwargs)
        print("Processing completed")
        return result
    return wrapper
@ad
def process_marks(marks,operation):
    return list(map(operation,marks))
marks=[40,45,60,32]
add = lambda x: x + 5
double = lambda x: x * 2
greater = lambda x: x > 40
print("Add Grace Marks:", process_marks(marks, add))
print("Double Marks:", process_marks(marks, double))
print("Greater than 40:", process_marks(marks, greater))
