#write a python program to built a basic swiggy food ordering system using variables
#using username,user id,delivary time ,card values,order details
#swiggy
personal_details={"username":"Nithin","user_id":"nithin215","email":"nithinkumar@gmail.com"}
order_item="biriyani"
delivery_time=10
cart_value=1
order_details={""}
print(order_details)
print(order_item)
print(delivery_time)
print(cart_value)
print(personal_details)

'''Write a function simple_interest(principal, rate=5, time=1) to calculate simple interest. 
Demonstrate different function calls by passing only required arguments and then overriding
 default values'''
def simple_interest(principal,rate=5,time=1):
    simp_interest=principal*rate*time/100
    print(simp_interest)
simple_interest(int(input("enter the principal amount :")))

'''Create a function student_info(name, *subjects, **details) that prints a student’s name,
 subjects enrolled, and additional details like grade and school.'''
def student_info(name,*subjects,**details):
    print("name:",name)
    for subject in subjects:
        print("subjects:",subject)
    for key,value in details.items():
        print(key,":",value)
student_info("nithin","java","python","css",
             roll_no="215",
             cls="B-tech",
             rank=3)

'''Write a function order_food(*items, **preferences) that accepts multiple food items and 
optional preferences like spice level or delivery time. Display the order summary'''

def order_food(*items,**preferences):
    print("order summary")
    print("items ordered")
    for item in items:
        print("items :",item)
    print("\npreferences")
    for key,value in preferences.items():
        print(key,":",value)
order_food("ice cream","biscuits","chocolate",
           south_india="idle",
           north_india="vadapav")

'''Write a function shopping_cart(discount=0, *prices) that calculates the total price after applying 
a discount. Demonstrate calling the function with and without the discount argument'''

def shopping_cart(discount=0,*prices):
    total_price=sum(prices)-discount
    print("total price:",total_price)
    for price in prices:
        print("prices",price)
shopping_cart(100,500,40)

'''Design a function register_user(username, role="user", *permissions, **details) that stores user
 information, including optional permissions and additional attributes'''

def register_user(username,role="user",*permissions,**details):
    print("username : ",username)
    print("role: ",role)
    for permission in permissions:
        print("permissions: ",permission)
    print("\n details")
    for key,values in details.items():
        print(key,":",values)
register_user("nithin","user","library","portal",
              user_id=215,
              address="kphb",
              college="mbu")
'''Define a function login(username, password="1234"). Demonstrate how default arguments work and 
explain a potential issue with using default passwords.'''

def function_login(username,password="1234"):
    print("username: ",username)
    print("password:",password)
function_login("nithin kumar")

'''Write a function calculate_score(base_score=0, *bonus_points, **penalties) that computes a final score
 after adding bonuses and subtracting penalties'''

def calculate_score(base_score=0,*bonus_points,**penalties):
    total_bonus=sum(bonus_points)
    total_penalty=sum(penalties.values())
    final_score=base_score+total_bonus-total_penalty

    print("base score:",base_score)
    for bonus_point in bonus_points:
        print("bonus points:",bonus_point)
    print("\n penalties")
    for key,values in penalties.items():
        print(key,":",values)
    print("\nfinal score",final_score)
calculate_score(50,10,
                fine=5)

'''Design a function send_email(sender, receiver, subject="No Subject", *attachments, **options) that simulates
 sending an email with optional attachments and settings'''

def send_email(sender,receiver,subject="No Subject",*attachments,**options):
    print("sender mail:",sender)
    print("receiver mail:",receiver)
    print("subject:",subject)
    print("\n attachments")
    for attachment in attachments:
        print("attachments :",attachment)
    print("\noptions")
    for key,value in options.items():
        print(key,":",value)
send_email("nithin@gmail.com","sai@gmail.com","","pdf","photo",
           To=" main recipients",
           cc="Subject Line")
