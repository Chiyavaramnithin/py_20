l = [1,2,3,4,5]
for i in l:
    print(i)

it = iter(l)
it = l.__iter__()
print(it)

print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())

class A:
    def __init__(self):
        self.val = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.val <= 5:
            num = self.val
            self.val += 1
            return num
        else:
            raise StopIteration

obj = A()
for i in obj:
    print(i)

print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
obj2 = A()
print(obj2.__next__())
print(next(obj2))
l = list(range(1, 11))
print(l)
class Numbers:
    def __init__(self, start, end):
        self.val = start
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.val <= self.end:
            current = self.val
            self.val += 1
            return current
        else:
            raise StopIteration
five_to_ten = Numbers(5, 10)
# for i in five_to_ten:
#     print(i)

twenty_to_hundred = Numbers(20, 100)
# for i in twenty_to_hundred:
#     print(i)

class Fibonacci:
    def __init__(self, n):
        self.count = 1
        self.n = n
        self.a , self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count <= self.n:
            val = self.a
            self.a, self.b = self.b, self.a + self.b
            self.count += 1
            return val
        else:
            raise StopIteration
five = Fibonacci(5)
# for i in five:
#     print(i)
#
ten = Fibonacci(10)
for i in ten:
    print(i)
class A:
    c1 = "hey"
    c2 = 123
    def __init__(self, x, y):
        self.x = x
        self.y = y
class B(A):
    c3 = True
    def __init__(self, z, x, y):
        self.z = z
        # A.__init__(self,x, y)
        super().__init__(x, y)
b = B(10, 20, 30)
print(b.c1)
print(b.c2)
print(b.c3)
print("z :",b.z)
print("x :",b.x)
print("y :",b.y)
class A:
    def __init__(self, x):
        self.x = x
class B(A):
    def __init__(self, x , y):
        self.y = y
        # A.__init__(self, x)
        super().__init__(x)
class C(B):
    def __init__(self, x, y , z):
        self.z = z
        # B.__init__(self, x, y)
        super().__init__(x, y)
c = C(10, 20 , 30)
print("x: ",c.x)
print("y :",c.y)
print("z :" ,c.z)