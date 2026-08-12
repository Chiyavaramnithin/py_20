'''Given a list of integers, filter numbers divisible by both 2 and 5, add 5 to each using map(),
then find the product using reduce().'''
from functools import reduce
lst=[20,3,50,7,1,10,15]
product=list(map(lambda x:x+5,list(filter(lambda x:x%2==0  and x%5==0,lst))))
print(product)
print(reduce(lambda x,y:x*y,product))

'''4. Given a list of integers, write a program to:

* Filter numbers divisible by 2 but not by 4
* Add 3 to each using map()
* Sort the result in descending order
* Find the product of all elements using reduce()'''

from functools import reduce
lst=[2,4,6,8,10,12,5,20]
result=list(map(lambda x:x+3,list(filter(lambda x:x%2==0 and x%4!=0,lst))))
desc=list(sorted(result,reverse=True))
print(desc)
print(reduce(lambda x,y:x+y,desc))

'''1. Given a list of tuples (name, marks), sort the list:
    * first by marks (descending)
    * then by name (ascending)'''
student=[
    {"name":"Aithin","score":78},
    {"name":"Bikhil","score":89},
    {"name":"sai","score":48},
    {"name":"Crinesh","score":88}
    ]
print(sorted(student, key=lambda x:x['score'],reverse=True))
print(sorted(student,key=lambda x:x['name']))

'''2. Given a list of strings, sort them based on:
    * length of string
    * and then alphabetically'''
name=['nithin','nikhil','trinesh','abhi']
print(sorted(name,key=lambda x:len(x),reverse=True))
print(sorted(name,key=lambda x:x))

'''6. Given a list of transactions where each transaction contains a type (credit or debit) and an amount, 
write a program to filter only the credit transactions, apply a 5% bonus to each transaction amount using map(), 
sort the updated transactions in descending order based on the amount, 
and finally compute the total credited amount using reduce().
INPUT: 
transactions = [
    {"type": "credit", "amount": 1000},
    {"type": "debit", "amount": 500},
    {"type": "credit", "amount": 2000}
]'''
from functools import reduce
transactions = [
    {"type": "credit", "amount": 1000},
    {"type": "debit", "amount": 500},
    {"type": "credit", "amount": 2000}
]
l=list(map(lambda x:x["amount"]*1.05,(list(filter(lambda x:x['type']=="credit",transactions)))))
print(reduce(lambda x,y:x+y,sorted(l,key=lambda x:x,reverse=True)))
