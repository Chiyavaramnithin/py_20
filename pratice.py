#add and sub varibles are merge and used to multiply and the multiplication variable should divide with n/10
def add_sub_multi_div(a,b,c,d):
    return((a+b),(c-d),((a+b)*(c-d)),(((a+b)*(c-d)))/10)
print(add_sub_multi_div(10,20,30,40))
# product of three numbers 1st
def multiply(a,b,c):
    return a*b*c
print(multiply(10,20,30))
#function of pet 2nd
def describe_pet(animal,name):
    print("My",animal,"is named",name)
describe_pet(animal="[animal]",name="[name]")
#4th
def power(base,exponent):
    return base ** exponent
print(power(4,5))
#5th
def full_name(first,middle,last):
    return first+middle+last
print(full_name("nithin","kumar","reddy"))

'''create a function and cal bill with parameters price and quantity that return cost and add 40 rs delivery fee 
if total is less than 200rs call in one line print result'''
def bill(price,quantity):
    cost=price*quantity
    if(cost<200):
        cost=cost+40
    return cost
print(bill(100,3))
#another method
def bill_1(price,quality):
    total=price*quality
    if(total<200):
        print("with delvery fee extra 40rs")
        total=total+40
    return total
print(bill_1(int(input("enter the price")),int(input("enter the quality"))))

'''create a python program to develop a simple atm system where a user attempts to withdraw money or deposit money
your application should verify if suff balance is avalible then these display the remaining balance impliment
these using multiple function like deposite, withdraw,checkbalance.and produce the final output in a single
 statement.'''
def deposite(balance,amount):
    balance=balance+amount
    return balance
def withdraw(balance,amount):
    if(amount<=balance):
        balance=balance-amount
    else:
        print("not enough balance")
    return balance
def check_balance(balance):
    return balance
balance=100000
print(check_balance(balance))
print(withdraw(balance,1000))
'''create a python application with  3 function. 1.total with 3 parameters of 3 subtraction.2 average with parameters
 with total and give average'''
def total(sub1,sub2,sub3):
    return sub1+sub2+sub3
print(total(10,20,30))
def average(sub1,sub2,sub3):
    average=sub1+sub2+sub3/3
    return average
print(average(10,20,30))
"""create a python application with 3 functions first fun name total with 3 parameters of 3 sub marks
avg func
grade that takes avg as input and if avg is greater than 85 perc return a grade if avg is abv 75 perc return b grade
if avg is 75 to 65 return c grade 50 percent to 65 return d grade , else retun fail call it in a single line" !!"""
def grade(avg):
    if avg>=85:
        return "A"
    elif avg>=75:
        return "B"
    elif avg>=65:
        return "C"
    elif avg>=50:
        return "D"
    else:
        return "Fail"
print(grade(int(input("enter the grade"))))