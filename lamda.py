def add(x,y):
    return x+y
print(add(10,20))

add1=lambda x,y:x+y
print(add1(10,20))

square=lambda x:x**2
print(square(5))

l=[3,7,4,6,29,9,14]
l.sort(key=lambda x:x%2)
print(l)

fruits=[(1,'banana'),(2,'apple'),(3,'cherry')]
fruits.sort(key=lambda x:x[1])
print(fruits)

cube=lambda x:x**3
print(cube(2))

large=lambda x,y: x if x>y else y
print(large(10,20))
'''Q1. Write a lambda to calculate simple interest.
Formula: (P * R * T) / 100'''
simple=lambda p,t,r:p*t*r
print(simple(10,20,10)/100)

'''Q2. Temperature Converter
Write a lambda to convert Celsius to Fahrenheit.
Formula: (C * 9/5) + 32'''
temperature=lambda x: (x*9/5)+32
print(temperature(100))

'''Q3. Electricity Bill
Write a lambda that calculates bill amount:
* If units ≤ 100 → ₹5/unit
* Else → ₹8/unit'''
electricity=lambda x:x*5 if x<=100 else x*8
print(electricity(10))

'''Q4. Login Check
Write a lambda that checks if username equals "admin" and password equals "1234" and returns "Login Success" or "Invalid".'''
login = lambda username, password: "Login Success" if username == "admin" and password == "1234" else "Invalid"
print(login("admin","1234"))
'''map()'''
l=[1,2,3,4]
p=list(map(lambda x:x**2,l))
print(p)
x=list(map(square,l))

l1=[1,2,3,4]
l2=[5,6,7,8]
result=list(map(lambda x,y:x+y,l1,l2))
print(result)

l1=[1,2,3,4]
l2=[5,6,7,8]
p=list(map(lambda x,y:x//2,l1,l2))
print(p)

even=lambda x: (x,"even") if x%2==0 else (x,"odd")
print(even(24))

l1=[1,2,3,4]
list(map(lambda x:x**2,l))
print(p)
print(list(filter(lambda x:x%2==0,p)))

'''An online store stores product prices in a list. Write a program using map() to apply a 10% tax to each product
 price and display the updated prices.'''
price=[100,200,300,67]
p=list(map(lambda x:x+(x*0.10),price))
print(p)
'''A list of usernames is stored in lowercase. Use map() to format them so that the first letter is uppercase.'''
username=['nithin','trinesh','nikhil']
updated_username=list(map(lambda x:x.capitalize(),username)) # capitalize is used to modify the name with the capital only the starting alphabet
print(updated_username)
'''An e-commerce website wants to display only products priced above ₹500. Use filter() to extract those prices from a list'''
prices=[200,300,7654,500,600,3000,700,800]
higher_prices=list(filter(lambda x : x>500,prices))
print(higher_prices)
'''Write a program that uses map() to calculate the length of each word in a list of strings'''
username=['nithin','trinesh','nikhil','purna']
length=list(map(lambda x:len(x),username))
print(length)
'''Given a list of integers, use filter() to select numbers greater than 50.'''
money=[80,35,45,67,89,12,23,34]
h=list(filter(lambda x:x>40,money))
print(h)
'''Use map() with a lambda function to multiply each number in a list by 5'''
num=[5,6,7,8,9]
n=list(map(lambda x:x*5,num))
print(n)
'''Use filter() with a lambda function to select numbers that are multiples of 4.'''
nums=[2,4,8,12,24]
final=list(filter(lambda x:x//4,nums))
print(final)