us=0
username="nithin"
password="nithin@1234"
def login(username,password):
    global us
    if username=="nithin" and password=="nithin@1234":
        us=us+1
        print("login sucessfull")
        return True
    else:
        print("invalid username or password")
        return False
for i in range(3):
    user=input("enter the username")
    pwd=input("enter the password")
    if login(user,pwd):
        break
else:
    print("Account is locked")
'''A system wants to track the number of times the login() function is called. Create a global variable attempts = 0
 and a decorator track_attempts that increments the global variable every time the login function is executed.
The login() function should accept username and password as parameters and display "Login attempted by <username>".
Call the function three times with different usernames and passwords, and finally display the total number of login
attempts. Use the global keyword inside the decorator to modify the global variable.'''

attempts=0
def login(func):
    def wrapper(login,password,*args,**kwargs):
        global attempts
        attempts+=1
        return func(login,password,*args,**kwargs)
    return wrapper
@login
def logins(username,password):
    print("username:",username)
    print("password",password)
logins("nithin","nithin@1234")
logins("trinesh","trinesh@1234")
logins("nikhil","nikhil@1234")
print("total no of attempts: ",attempts)

'''An ATM system has a function withdraw(username, pin, amount). Create a decorator authenticate that checks whether
the username is "admin" and PIN is "1234". If authentication is successful, execute the function; otherwise, display
"Invalid credentials". The function should maintain a global balance = 10000, deduct the amount if sufficient balance
exists, and display the remaining balance.'''

balance=10000
def authentication(func):
    def wrapper(username,pin,amount):
        if username=="admin" and pin=="1234":
            print("authentication successful")
            return func(username,pin,amount)
        else:
            print("Invalid credentials")
            return None
    return wrapper
@authentication
def withdraw(username,pin,amount):
    global balance
    if amount<=balance:
        balance-=amount
        print(f"Withdrawal successful! Remaining balance: {balance}")
    else:
        print("Insufficient balance!")
withdraw("admin","1234",int(input()))

'''An online examination system has a function start_exam(username, password, exam_name). Create a decorator
login_required to authenticate the student and another decorator track_attempt to count how many times the exam
is started. If authentication is successful, display "Exam started for <username>" along with the exam name. Finally,
display the total number of exam attempts.'''

attempts=0
def authenticate(func):
    def wrapper(username,password,exam_name):
        if username=="nithin" and password=="nithin@1234":
            global attempts
            attempts+=1
            print("authentication successful")
            return func(username,password,exam_name)
        else:
            print("invalid authentication")
            return None
    return wrapper
@authenticate
def start_exam(username,password,exam_name):
    print(f"Total exam attempts: {attempts}")
    print(f"Exam started for {username} - {exam_name}")
start_exam("nithin", "nithin@1234", "Python Basics")

username="nithin"
password="nithin@123"
usa=0
sa=0
def dec(func):
    def wrapper(*args,**kwargs):
        print("Application start")
        func(*args,**kwargs)
    return wrapper

@dec
def login(username1,password1):
    global sa,usa
    if(username1==username and password1==password):
        sa += 1
        print("Login Successful")
    elif(username1!=username):
        usa += 1
        if(usa<=3):
            x = input("Enter username:")
            login(x,password1)
        else:
            print("No more Attempts")
    else:
        usa += 1
        if(usa<=3):
            x = input("Enter your password:")
            login(username1,x)
        else:
            print("No more attempts")
login(input(),input())
print(sa)
print(usa)