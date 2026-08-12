user_name = "nithinkumar215"
print(user_name)
print(type(user_name))
password = "Nithin@12345"
print(password)
print(type(password))
Age = 21
print(Age)
print(type(Age))
seats = "21B"
print(seats)
print(type(seats))


a=int(input("enter a number:"))
if (a>=100 and a<=1000):
    if(a%2==0):
        print(a%3)
    else:
        print(a%2)
else:
    print("wrong number")


a=int(input())
if a<2:
    print("Invalid range")
else:
    fc=0
    for i in range(1,a+1):
        if a%i==0:
            fc=fc+1
    if fc==2:
        print(a)
    else:
        lower=a-1
        upper=a+1
        while True:
            if lower>=2:
                fcl=0
                for i in range(1,lower+1):
                    if lower%i==0:
                        fcl+=1
                if fcl==2:
                    print(lower)
                    break
            fcu=0
            for i in range(1,upper+1):
                if upper%i==0:
                    fcu+=1
            if fcu==2:
                print(upper)
                break
            lower-=1
            upper+=1



