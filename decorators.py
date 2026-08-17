def outer():
    def inner():
        print("hi")
    inner()
    return inner
func=outer()
func()
#1
def greet(name):
    print("my name is",name)
def m1():
    print("hi!")
m1()
greet("kulfi")
#2 same as #1
def m1(func):
    print("hi")
    func("kulfi")
m1(greet)

'''decorators with *args and **kwargs'''
def my_decorator(func):
    def wrapper(*args,**kwargs):
        print("Before")
        result=func(*args,**kwargs)
        print("After")
        return result
    return wrapper
def add(a,b):
    return a+b
add(10,90)

'''1.     Create a function place_order(item)
    Write a decorator that prints:
    * “Function started” before execution
    * “Function ended” after execution'''

def start_system():
    print("Starting system")
def dec1(func):
    def wrapper1():
        func()
        print("System started")
    return wrapper1
x=dec1(start_system)
x()

'''2.     Create a function show_message()
    Write a decorator that prints:
    * “Welcome!” before
    * “Goodbye!” after'''

def show_message():
    print("welcome! before")
def dec2(func):
    def wrapper1():
        print("Hi")
        func()
        print("Goodbye! after")
    return wrapper1
y=dec2(show_message)
y()

'''3.     Create a function make_payment()
    Write a decorator that prints:
    * “Payment initiated”
    * “Payment successful'''

def make_payment():
    print("payment initiated")
def dec3(func):
    def wrapper2():
        func()
        print("payment successful")
    return wrapper2
make_payment()
print("after adding decorator")
x=dec3(make_payment)
x()

def decorator1(func):
    def wrapper(*args,**kwargs):
        print("before calling")
        func(*args,**kwargs)
        print("after calling")
    return wrapper
@decorator1
def add(a,b):
    print(a+b)
add(10,20)

'''Create a function get_message() that returns "hello user". Write a decorator using @ syntax that converts
 the output to uppercase.'''
def decorator1(func):
    def wrapper(*args,**kwargs):
        print("before ")
        func(*args,**kwargs)
        print("after uppercase")
    return wrapper
@decorator1
def get_message(msg):
    print(msg.upper())
get_message("nithin")

'''  Create a function get_number() that returns 10
    Use a decorator to return double the value.'''
def double(func):
    def wrapper(*args,**kwargs):
        print("before double")
        func(*args,**kwargs)
        print("after double")
    return wrapper
@double
def get_number(num):
    print(num*2)
get_number(10)

'''.     Create a function place_order(item)
    Use a decorator to print:
    * “Order process started”
    * “Order process completed”'''

def place_order(item):
    def wrapper(*args,**kwargs):
        print("order process started")
        item(*args,**kwargs)
        print("order process completed")
    return wrapper
@place_order
def order(items):
    print(items,"your items is ready to deliver")
order("honey,chips,ots")

'''4.     Create a function login(username)
    Use a decorator to print:
    * “Authenticating user…”
    * “Login successful'''

def login(username):
    def wrapper(*args,**kwargs):
        print("Authenticating user")
        username(*args,**kwargs)
        print("Login successful")
    return wrapper
@login
def decorator2(name):
    print(name,"username")
decorator2("nithin")


'''.     Create a function send_message(msg)
    Use a decorator to print:
    * “Sending message…”
    * “Message sent”'''

def message(func):
    def wrapper(*args,**kwargs):
        print("sending message")
        func(*args,**kwargs)
        print("message sent")
    return wrapper
@message
def send_message(msg):
    print(msg)
send_message("hello")

'''Create a function add(a, b)
    Use a decorator to print:
    * “Calculating sum…”
    * “Calculation done”'''

def decorator3(func):
    def wrapper(*args,**kwargs):
        print("before Calculating sum")
        func(*args,**kwargs)
        print("after calculating sum")
    return wrapper
@decorator3
def add(a,b):
    print(a+b)
add(10,20)

'''A banking application has a function check_balance(). Create two decorators: verify_user, which prints
 "User verified", and log_transaction, which prints "Transaction logged". Apply both decorators to 
 check_balance() and display "Balance displayed" from the original function.'''
def verify_user(func):
    def wrap1(*args,**kwargs):
        print("User verified")
        func(*args,**kwargs)
    return wrap1
def log_transaction(func):
    def wrap2(*args,**kwargs):
        print("Transaction logged")
        func(*args,**kwargs)
    return wrap2
@verify_user
@log_transaction
def check_balance(balance):
    print("Balance displayed")
check_balance(verify_user(log_transaction(check_balance)))
check_balance(1000)

'''An online examination system has a function start_exam(student). Before allowing the student to start
 the exam, the system must verify the student’s login and then log the exam activity. 
 Create two decorators, login_required and log_activity, and apply both decorators to start_exam(). 
 The function should finally display "Exam started for <student>".'''

def verify_login(func):
    def warp1(*args,**kwargs):
        print("login requried")
        func(*args,**kwargs)
    return warp1
def login_activity(func):
    def wrap2(*args,**kwargs):
        print("login acitivity")
        func(*args,**kwargs)
    return wrap2
#@login_activity
#@verify_login
def start_exam(student):
    print(f"exam started for {student}")
start_exam=verify_login(login_activity(start_exam))
start_exam("nithin")

'''An online shopping application has a function place_order(). Create two decorators: 
login_check to print "Login verified" and order_log to print "Order recorded".
 Apply both decorators to place_order() and display "Order placed successfully" from 
 the original function.'''

def login_check(func):
    def warp1(*args,**kwargs):
        print("login verified")
        func(*args,**kwargs)
    return warp1
def order_log(func):
    def wrap2(*args,**kwargs):
        print("order recorded")
        func(*args,**kwargs)
    return wrap2
@login_activity
@verify_login
def place_order():
    print("order placed successfully")
place_order()

#seperate question
def log_deco(func):
    def wrap(*args):
        print("values",args)
        result=func(*args)
        print(result)
        return result
    return wrap
def greater_first(func):
    def wrap(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return wrap
@log_deco
@greater_first
def sub(a,b):
    return a-b
result=sub(2,4)
print(result)
@log_deco
def add(a,b,c):
    return a+b+c
result1=add(1,2,3)
print(result1)