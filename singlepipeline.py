l=[10,20,34,50,60]
l2=list(filter(lambda x:x>50,list(map(lambda x:x+x*0.10,l))))
print(l2)

'''Given a list of product prices, write a program to:

* Filter prices greater than ₹500
* Apply a 10% discount to the filtered prices using map()'''

prices=[200,400,500,6776,767,998]
l2=list(filter(lambda x:x>500,list(map(lambda x:x-x*0.10,prices))))
print(l2)

'''Given a list of integers, write a program to filter even numbers and then multiply each of them by 3 using a single pipeline'''
lst=[10,20,30,40,56,3]
even=list(map(lambda x:x*3,list(filter(lambda x:x%2==0,lst))))
print(even)

'''Given a list of numbers, write a program to filter numbers greater than 20 and then square each of the filtered numbers using map().'''
num=[1,3,4,67,8,2]
square=list(map(lambda x:x**2,list(filter(lambda x:x>20,num))))
print(square)

'''Given a list of words, write a program to filter words whose length is greater than 4 and then convert those words into uppercase
 using a single pipeline'''
name=['nithin','trinesh','nikhil','sai']
lst=list(map(lambda x:x.upper(),list(filter(lambda x:len(x)>4,name))))
print(lst)

'''Given a list of integers, write a program to filter numbers divisible by 5 and then add 10 to each of the filtered numbers.'''
lst=[23,45,67,86,55]
l1=list(map(lambda x:x+10,list(filter(lambda x:x%5==0,lst))))
print(l1)

'''Given a list of student marks, write a program to filter students who scored more than 40 and then increase their marks by 5 using map()'''
marks=[44,45,46,78,60,50,33,21]
student_marks=list(map(lambda x:x+5,list(filter(lambda x:x>40,marks))))
print(student_marks)

#reduce
from functools import reduce
l=[1,2,3,4,7,9,14]
print(reduce(lambda x,y:x+y,l))

'''Given a list of strings, write a program using reduce() to concatenate all strings into a single string.'''
from functools import reduce
lst=["nithn","kumar","reddy"]
print(reduce(lambda x,y:x+y,lst))

'''Given a list of digits, write a program using reduce() to form a single number (e.g., [1,2,3] → 123)'''
from functools import reduce
digits=[1,2,4,5,7,9]
print(reduce(lambda x,y:x*10+y,digits))

'''Given a list of student marks, write a program using reduce() to find the total marks and then compute the average'''
from functools import reduce
marks=[30,40,50,60,70]
print(reduce(lambda x,y:x+y,marks)/len(marks))

#sorted
'''syntax=sorted(iterable,key=func,reverse=(true or false))'''
students=[{'name':'Alice','score':85},
          {'name':'hary','score':79},
          {'name':'nithin','score':97}]
print(sorted(students,key=lambda x:x['score']))
print(sorted(students,key=lambda x:len(x['name']))) # for printing the length of the names in ascending order
print(sorted(students,key=lambda x:x['score'],reverse=True)) # printing descending order

'''use map() to convert a list of temperature in celsius to fahrenheit '''
l=[40,80]
l1=list(map(lambda x:(x*9/5)+32,l))
print(l1)

'''use filter to extract all words from a list that start with capital letter'''
l=['Nithin','Kumar','reddy']
l1=list(filter(lambda x:x[0].isupper(),l))
print(l1)

'''use reduce() to find the product of all numbers in a list'''
from functools import reduce
l=[1,2,3,4,5]
print(reduce(lambda x,y:x*y,l))

'''sort a list of tuples(name,age) by age in descending order using sorted() with a lambda key'''
person=({'name':'nithin','age':21},
        {'name':'nikhil','age':22})
print(sorted(person,key=lambda x:x['age']))

'''chain map() and filter() from[1 to 10] first filter out odds then square the remaining evens'''
l=[1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x:x**2,list(filter(lambda x:x%2==0,l)))))

'''use reduce() to find the longest string in a list '''
from functools import reduce
l=['cat','elephant','dog','rhinoceros']
print(reduce(lambda x,y:x if len(x) > len(y) else y,l))

'''write your own version of map() called my_map(func,lst) using a regular loop verify it gives the same results as a built in'''
def my_map(func,lst):
    result=[]
    for i in lst:
        x=func(i)
        result.append(x)
    return result
def square(x):
    return x**2
l=[10,20,45,30]
print(list(filter(lambda x:x>500,my_map(square,l))))
