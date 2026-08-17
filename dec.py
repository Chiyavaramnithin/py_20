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