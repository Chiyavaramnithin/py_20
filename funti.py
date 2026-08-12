
def add_sub_multi(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c,d,e)
add_sub_multi(5,6,)
# finding area of rectangle
def area_of_rectangle(length,width):
    x=length*width
    return x
print(area_of_rectangle(5,5))

sum=56
for i in range(57,154):
    sum+=i
print(sum)

for i in range(700,901):
    if i%2==0:
        print(i)
# Assign the builtin function len to a variable called count use it to find the length of a list

count = len
lst1 = [10, 20, 30, 40, 50]
length = count(lst1)
print("Length of the list:", length)

# write a function run_twice(func,value) that calls fanc on value twice and returns the final result
def run_twice(func,value):
    result = func(value)
    final_result=func(result)
    return final_result
print(run_twice(abs,5))

#store the function upper,lower,title(string method) in a dictionary let the user choose which one to apply
string_methods={
    "1":str.upper,
    "2":str.lower,
    "3":str.title
}
user_text= input("enter the text :")
print("\nChoose an option:")
print("1: Uppercase")
print("2: Lowercase")
print("3: Title Case")
choice = input("Enter choice (1, 2, or 3): ")
if choice in string_methods:
    select=string_methods[choice]
    result=select(user_text)
    print(f"\nResult: {result}")
else:
    print("\nInvalid choice selected.")

#write a function that returns another function example make_multiplier(3) should return a function that multiplies any number by 3
def make_multiplier(number):
    def multiplier(x):
        return number* x
    return multiplier
