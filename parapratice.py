#1
def say_hello():
    print('Welcome to python!')
def add(a,b):
    c=a+b
    print(c)
def m1():
    print('nithin')
def area_of_rectangle(length,width):
    return length*width
print(area_of_rectangle(6,4))
say_hello()
add(5,6)
m1()

'''write a function power(base,exponent=2) that returns base^exponent. test with one and two arguments'''
def power(base,exponent=2):
    return base**exponent
print(power(base=4))
print(power(3,4))
print(power(exponent=3,base=4))

'''create a function connect(host,port=3306,protocol='tcp') and call it with various combinations'''
def connect(host,port=3306,protocal='TCP'):
    return host,port,protocal
print(connect(host='local host'))

'''finding the discount price'''
def discount_price(price,discount=10):
    final_price=price-(price*discount/100)
    return final_price
print(discount_price(1000))
print(discount_price(price=1200))
#parameters and arguments
def m1():
    print('hi class!')
    return 10
m1()
print(m1())
'''syntax :
def<fun name>(<param>):
<lines of code>'''
def m1(x):
    print(x)
m1(10/2)
m1(10//2)
m1(10%2)
m1(10**2)


def learn(name,skill):
    print("hi!",name,"is learning",skill)
learn("nithin","python")
def skill(user,id):
    print("hi!",user,"skill is",id)
skill("nithin","python")
def add(a,b):
    return a+b
print(add(int(input("Enter a number")),int(input("Enter another number"))))
def w1():
    print("welcome to python")
w1()