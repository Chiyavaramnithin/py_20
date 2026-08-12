#shallow copy nested list
import copy
list1=[[1,2],[3,4]]
list2=list1.copy()
list1[1][1]=100
print(list1)
list1[1][0]=200
print(list2)
#deep copy
list1[1][0]=100
print(list1)
list2=copy.deepcopy(list1)
print(list2)

''' map() + filter() + lambda: Given a list of integers from 1 to 20, use filter() to keep multiples of 3,
 then use map() to square them. Print the result. '''
l=[i for i in range(1,21)]
lst=list(map(lambda x:x**2,list(filter(lambda x:x%3==0,l))))
print(lst)

'''Q1.  PARAMETERS + LAMBDA: Write a function apply_operation(a, b, op) where op is a lambda. Call it with
 operations for add, subtract, and multiply. '''
def apply_operation(a,b,op):
    return op(a,b)
print(apply_operation(10,5,lambda x,y:x+y))
print(apply_operation(10,5,lambda x,y:x-y))
print(apply_operation(10,5,lambda x,y:x*y))
'''Q4. **kwargs + reduce(): Write a function weighted_average(**scores) where keys are subjects and values are scores. 
Use reduce() to compute the average of all values. '''

from functools import reduce
def weighted_average(**scores):
    values=list(scores.values())
    total=reduce(lambda x,y:x+y,values)
    average=total/len(values) if values else 0
    return average
print(weighted_average(math=51,science=60,pyhton=70,java=80))

'''Q3.  DEFAULT + KEYWORD + LAMBDA: Write a function make_greeting(name, prefix='Hello', formatter=lambda x: x)
 that applies formatter to the final greeting string. Test with str.upper as the formatter. '''

def make_greeting(name,prefix='Hello',formatter=lambda x:x):
    a=f"{prefix}{name}"
    return formatter(a)
print(make_greeting('nithin',prefix="hie",formatter=lambda x:x.upper()))

'''from functools import reduce
def sum_of_square(*args):
    square=map(lambda x:x**2,args)
    total=reduce(lambda x,y:x+y,square)
    return total
print(sum_of_square(1,2,3,4,5))


def even_numbers(*args):
    even=filter(lambda x:x%2==0,args)
    num=sorted(even,key=lambda x:x)
    return num
print(even_numbers(2,4,7,5,3,2,8))

def rank_students(**scores):
    marks=list(scores.items())
    total=sorted(marks,key=lambda x:x,reverse=True)
    return total
print(rank_students(alice=56,nithin=90,nikhil=89))'''

'''FUNCTION REFERENCE + HIGHER ORDER: Create a list of lambda functions [double, triple, quadruple]. 
Write a function apply_all(funcs, value) that applies each in sequence and returns the final result.'''
funcs=[
    lambda x:x*2,
    lambda x:x*3,
    lambda x:x*4
]
def apply_all(funcs,value):
    result=value
    for f in funcs:
        result=f(result)
    return result
print(apply_all(funcs,1))
print(apply_all(funcs,2))

'''funcs=[
    lambda x:x**2,
    lambda x:x+1,
    lambda x:x/2
]
def pipeline(funcs,value):
    result=value
    for f in funcs:
        result=f(result)
    return result
print(pipeline(funcs,3))

funcs=[
    lambda x:x.upper(),
    lambda x:x[::-1],      #for reverse order
    lambda x:x+"!"
]
def apply(funcs,value):
    result=value
    for f in funcs:
        result=f(result)
    return result
print(apply(funcs,"nithin"))'''

'''**kwargs + reduce(): Write a function weighted_average(**scores) where keys are subjects and values are scores.
 Use reduce() to compute the average of all values. '''

from functools import reduce
def weighted_average(**scores):
    values=list(scores.values())
    total=reduce(lambda x,y:x+y,values)
    average=total/len(values)
    return average
print(weighted_average(python=100,java=50,c=30))

'''Q8.  FULL PIPELINE: Build a mini data pipeline. Start with a list of student dictionaries [{name, score}]. 
Use filter() to keep scores >= 60, map() to add a 'grade' key ('Pass'), and sorted() to sort by score descending. 
Print the final result.'''

student=[
    {"name":"nithin","score":78},
    {"name":"nikhil","score":89},
    {"name":"sai","score":48}
]
passed=filter(lambda x:x['score']>=60,student)
grade=map(lambda x:{**x,"grade":"pass"},passed)
final_result=sorted(grade,key=lambda x:x['score'],reverse=True)
print(final_result)

'''Q9.  LAMBDA + sorted() + FUNCTION REFERENCE: Store three sort strategies in a dictionary: by_name, by_score,
 by_length. Let the user choose a strategy by name, then apply it to sort a list of tuples.'''

students=[
    ("nithin",78),
    ("trinesh",77),
    ("nikhil",80),
    ("purna",76)
]

strategies={
    "by_name":{"key": lambda x:x[0]},
    "by_score": {"key": lambda x:x[1],"reverse":True},
    "by_length":{"key": lambda x:len(x[0]),"reverse":False}
}
choice=input("choose strategies:")
if choice in strategies:
    a=strategies[choice]
    result= sorted(students, key=a["key"], reverse=a["reverse"])
    print(result)
else:
    print("invalid")

