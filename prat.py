#Write a function that takes two numbers as input and returns their sum.
'''def add(a,b):
    sum=a+b
    return sum
print(add(int(input("enter a number")),int(input("enter a number"))))
#Create a function that checks if a given number is even or odd.
def eve(a):
    if a%2==0:
        print("even")
    else:
        print("odd")
print(eve(int(input("enter a number"))))
#Define a function that takes a string and returns the number of vowels in it.
def count_vowels(text):
    vowels="aeiouAEIOU"
    count=0
    for char in text:
        if char in vowels:
            count+=1
    return count
print(count_vowels(input("enter a string")))
#Write a function that accepts a list and returns the largest element.
def largest(numbers):
    largest=numbers[0]
    for num in numbers:
        if num>largest:
            largest=num
    return largest
print(largest([10,20,30,45]))
#Create a function that reverses a string without using slicing.
def reverse(text):
    reversed_text=""
    for char in text:
        reversed_text=char+reversed_text
    return reversed_text
print(reverse("nithin"))'''

''' 1.Given a list of product prices, write a program to filter prices above ₹500, then apply a 10% discount using
 map(), and compute the final total bill using reduce().'''
from functools import reduce
l=[100,200,400,600,700,800]
prices=list(map(lambda x:x-x*0.10,list(filter(lambda x:x>500,l))))
print(prices)
print(reduce(lambda x,y:x+y,prices))
''' 2.Given a list of numbers, write a program to filter negative numbers, then convert them into positive numbers
 using map(), and find their sum using reduce().'''
from functools import reduce
l=[-1,2,-1,4,-4,8,-7]
sum=list(map(lambda x:x*(-1),list(filter(lambda x:x<0,l))))
print(sum)
print(reduce(lambda x,y:x+y,sum))
''' 3.Given a list of integers, write a program to filter numbers less than 50, then multiply each by 3 using map(),
 and determine the maximum value using reduce().'''
from functools import reduce
l=[30.45,50,55,60,56]
multi=list(map(lambda x:x*3,list(filter(lambda x:x>50,l))))
print(multi)
print(reduce(lambda x,y:x if x>y else y,multi))
''' 4.Given a list of words, write a program to filter words with length greater than 3, then convert them to
 uppercase using map(), and concatenate them into a single string using reduce().'''
from functools import reduce
l=["nithin","sai","nikhil","mad"]
words=list(map(lambda x:x.upper(),list(filter(lambda x:len(x)>3,l))))
print(words)
print(reduce(lambda x,y:x+y,words))
''' 5.A company tracks employee salaries. Write a program to filter salaries greater than ₹30,000, increase them
 by 15% using map(), and compute the total salary expenditure using reduce().'''
from functools import reduce
l=[31000,30000,38000,28000,60000]
salaries=list(map(lambda x:x+x*0.15,list(filter(lambda x:x>30000,l))))
print(salaries)
print(reduce(lambda x,y:x+y,salaries))
''' 6.A data analysis system stores a list of integers. Write a program to filter odd numbers, square each using
 map(), and compute their sum using reduce().'''
from functools import reduce
l=[1,2,3,4,5,6,7,8]
num=list(map(lambda x:x**2,list(filter(lambda x:x%2!=0,l))))
print(num)
print(reduce(lambda x,y:x+y,num))
''' 7.An e-commerce platform stores product prices in a list. Write a program to filter products priced above ₹500,
 apply a 10% discount to those products using map(), and then calculate the total bill amount using reduce().'''
from functools import reduce
l=[300,400,500,600,656,555]
product=list(map(lambda x:x-(x*0.10),list(filter(lambda x:x>500,l))))
print(product)
print(reduce(lambda x,y:x+y,product))
''' 8.A banking system stores transaction amounts. Write a program to filter only credit transactions (positive values), 
apply a processing bonus of ₹10 to each using map(), and calculate the total credited amount using reduce().'''
from functools import reduce
l=[1000,2000,-300,35,-500]
credit=list(map(lambda x:x+10,list(filter(lambda x:x>0,l))))
print(credit)
print(reduce(lambda x,y:x+y,credit))