contacts={'nithin','trinesh','pawan kalyan'}
messages={'hi','bye'}
print(id(contacts))
nithin={'username':'nithin','phone no':1234,'status':'busy'}
#messages+=['busy?']
print(id(messages))
print(id(nithin))

'''write a python program to build a simple uber application that has a function called trip details with parameters like 
driver name , pick up location , drop location , total price , called these function using positional arguments once
and keywords arguments once'''
def trip_details(driver_name, pick_up_location, drop_location, total_price):
    print("your driver name:" , driver_name)
    print("your pick up location:" , pick_up_location)
    print("your drop location:" , drop_location)
    print("your total price:" , total_price)
trip_details("sai","kphb","jntu",56) #positional arguments
trip_details(total_price=56,drop_location="jntu",driver_name="sai",pick_up_location="kphb") #keyword arguments
'''call the function send_email(to,subject,body) using keyword argument in any order'''
def send_email(to,subject,body):
    return to,subject,body
print(send_email("nithinchiyavaram@gmail.com","about the job description","saikumar@gmail.com"))

'''write a function create profile (username,email,age)and call it using keyword argument'''
def create_profile(username,email,age):
    return username,email,age
print(create_profile("nithin215","nithinchiyavaram@gmail.com","21"))

'''rewrite this call using keyword arguments book ticket (Alice,delhi,mumbai,2)'''
def book_ticket(passenger_name="Alice",from_location="Delhi",to_location="Mumbai",seat_number="2"):
    return passenger_name,from_location,to_location,seat_number
print(book_ticket())

'''write a function intro(name,city,hoggy) that prints a sentence about a person call it in two different orders
 and observe the difference'''
def intro(name,city,hobby):
    print("my name is,name",name)
    print("my city is,city",city)
    print("my hobby is,hobby",hobby)
intro("nithin","tirupathi","playing cricket")
intro(name="nithin",hobby="playing crickert",city="tirupathi")

'''create subtract (a,b) that returns a-b what is the difference between subtract(10,3) and subtract(3,10)'''
def subtract(a,b):
    c=a-b
    return c
print(subtract(int(input("Enter a number")),int(input("Enter another number"))))

'''write a function bio(first name.last name,age) and call it correctly using positional arguments'''
def bio(first_name,last_name,age):
    a=first_name,last_name,age
    return a
print(bio("nithin","reddy",21))
print(bio(age=21,last_name="reddy",first_name="nithin"))

'''can you pass more positional arguments than there are parameters what error do you get
def pass(first_name,last_name):
    c=first_name,last_name
    return c
print(pass("nithin","reddy",21))
output
#invalid syntax'''
