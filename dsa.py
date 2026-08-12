'''the elements will shows how many times it print
from operator import true'''

a=list(map(int,input().split()))
for i in range(len(a)):
    f=0
    for j in range(0,len(a)):
        if(a[i]==a[j]):
            f=f+1
    if(f==1):
        print(a[i],f)

'''This code always prints only the first element of the list, 
because the condition if f == 1 is satisfied only for i = 0.'''
a=list(map(int,input().split()))
for i in range(len(a)):
    f=0
    for j in range(i,-1,-1):
        f+=1
    if(f==1):
        print(a[i])

'''most repeated elements'''
a=list(map(int,input().split()))
x,y=0,0
for i in range(len(a)):
    f=0
    for j in range(0,len(a)):
        if(a[i]==a[j]):
            f=f+1
    if(f>x):
        x=f
        y=a[i]
print(x,y)

'''to find the unique value'''
a=list(map(int,input().split()))
for i in range(len(a)):
    f=0
    for j in range(0,len(a)):
        if(a[i]==a[j]):
            f+=1
    if(f==1):
        print(a[i],end=" ")

'''This code is essentially finding the common elements between two lists (a and b), 
respecting the frequency in b.'''
a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in range(len(a)):
    f=0;x=0
    for j in range(i,-1,-1):
        if(a[i]==a[j]):
            f=f+1
    for j in range(0,len(b)):
        if(a[i]==a[j]):
            x=x+1
    if(f<=x):
        print(a[i],end=" ")
'''printing the list in order'''
a=list(map(int,input().split()))
for i in range(len(a)-1):
    for j in range(len(a)-1-i):
        if(a[j]>a[j+1]):
            a[j],a[j+1]=a[j+1],a[j]
print(a)
'''This program validates whether the input string is either:

A 12-digit number (all digits), or

A 14-character string with spaces at positions 4 and 9, and digits everywhere else.'''
s=input()
t=False
if(len(s)==12 or len(s)==14):
    if(len(s)==12 and s.isdigit()):
        t=True
    else:
        c=0
        for i in range(len(s)):
            if((i==4 or i==9)and s[i]==" "):
                c+=1
            elif(i!=4 and i!=9 and s[i].isdigit()):
                c+=1
            else:
                c=0
                break
        if(c==0):
            t=False
        else:
            t=True
if(t):
    print("valid")
else:
    print("invalid")