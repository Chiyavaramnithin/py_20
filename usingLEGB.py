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

