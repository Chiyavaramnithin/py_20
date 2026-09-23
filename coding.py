# 2 Write a program to insert an element at a specific index in a list.
l=list(map(int,input().split()))
n=int(input())
i=int(input())
l.insert(i,n)
print(*l)

#3 Write a program to merge two lists into a single list.
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l=l1+l2
print(*l)
#4Write a program to remove a specific element from a list.
l=list(map(int,input().split()))
n=int(input())
if (n in l):
    l.remove(n)
    print(*l)
else:
    print("invalid input")

#5 Write a program to remove an element from a list using its index.
l=list(map(int,input().split()))
n=int(input())
if (n in l):
    k=l.index(n)
    print(k)
else:
    print("Invalid Input")

#6. Write a program to find the index of a given element in a list.
l=list(map(int,input().split()))
n=int(input())
for i in l:
    k=l.index(n)
    print(k)

#7. Write a program to count the number of occurrences of an element in a list.
l=list(map(int,input().split()))
n=int(input())
l1=l.count(n)
print(l1)
#8. Write a program to find the sum of the first and last elements of a list.
l=list(map(int,input().split()))
n=int(input())
if  (n>0 and n<len(l)):
    sum=0
    for i in range(n+1):
        sum=sum+l[i]
    print(sum)

#9. Write a program to calculate the sum of list elements up to a given index.
l=list(map(int,input().split()))
n=int(input())
if  (n>0 and n<len(l)):
    sum=0
    for i in range(n+1):
        sum=sum+l[i]
    print(sum)
#10. Write a program to calculate the average of odd numbers in a list.
l=list(map(int,input().split()))
sum=c=0
for i in range(len(l)):
    if (l[i]%2==1):
        sum=sum+l[i]
        c+=1
if c>0:
    print(sum/c)
else:
    print("Invalid input")

#11. Write a program to print all prime numbers present in a list.
l=list(map(int,input().split()))
for i in range(len(l)):
    fc=0
    for j in range(1,l[i]+1):
        if (l[i]%j==0):
            fc=fc+1
    if fc==2:
        print(l[i])