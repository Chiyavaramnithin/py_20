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