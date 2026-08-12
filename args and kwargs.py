'''*args are the positional arguments '''
def add(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
print(add(1,2,3))
'''**kwargs are the keyword arguments'''
#for **kwargs
def emp_details(**kwargs):
    # print(kwargs)
    for key, value in kwargs.items():
        print(key, ":",value)
emp_details(emp_name = "jude",
            emp_id = 2210,
            emp_salary = 1000000)
emp_details(emp_id = 20302,
            emp_salary = 200000,
            emp_name = "Candice",
            emp_designation =  " HR Exec",
            emp_department = "HR & RD")


'''create a python application to develop simple hospital billing system design function like cal bill with *args charges of variable type
 or orbitary type and other apply insurance with **kwargs of variable or orbitary type  and create a function add taxes with keyword args
of variable type the program should accepts the multiple charges like consultant ,treatment apply insurance deduction and apply tax'''
def hospital_billing(*args):
    total_bill=0
    for i in args:
        total_bill+=i
    return total_bill
def apply_insurance(amount,**kwargs):
    total_claim=0
    for key,value in kwargs.items():
        print(f"{key}: {value}")
        total_claim+=value
        return total_claim
def total_taxes(amount,**kwargs):
    total_tax=0
    for i in kwargs:
        for key,value in kwargs.items():
            print(f"{key}:{value}")
            total_tax+=value
            return amount-total_tax
total_bill=(hospital_billing(3000,4000,5000))
print("total bill:",total_bill)
total_claim=(apply_insurance(total_bill,lic1=1000,lic2=2000,lic3=4000))
print("after applying insurance:",total_bill)
total_taxex=(total_taxes(total_bill,gst=200,sgst=300))
print("after applying taxes:",total_taxex)

'''Design a Python program for a supermarket billing system. Create a function  calculate_total(*prices) that accepts 
the prices of multiple items and returns their total cost. Then define a function apply_discount(*amount) that applies
 a 10% discount if the total exceeds 1500. Finally, create a function final_bill(**details) that accepts keyword 
 arguments such as amount, tax, and packing_charge, and returns the final payable bill. Display the final amount
  using a single nested function call.'''

def calculate_total(*prices):
    total_bill=0
    for i in prices:
        total_bill+=i
    return total_bill
def apply_discount(*amount):
    total_cost=amount[0]
    for i in amount:
        if(total_cost>1500):
           return total_cost-(total_cost*0.10)
        return total_cost
def final_bill(**details):
    total_price=0
    for service,charges in details.items():
        print(service,":",charges)
        total_price+=charges
    print(total_price)
total_bill=(calculate_total(int(input("enter the ist item :")),int(input("enter the 2nd item :"))))
print("total bill:",total_bill)
total_cost=(apply_discount(total_bill))
print("after applying the discount:",total_cost)
total_price=(apply_discount(total_bill))
print("total price:",total_price)

'''create a python application to design a function for a food delivery application where the customer name is taken
 as a positional argument and the audio type default argument function should accepts multiple food items order 
 by the customer using positional arguments and additional details such as address, payment mode,delivery instrustion 
and using keyword arguments the function should display the complete order summary include the customer details list 
items ordered, total number of items, and all additional items'''

def swiggy(customer_name,order_type='regular',*items,**customer_details):
    print('Hi',customer_name)
    print('your order type',order_type)
    print('your cart',items)
    total_bill=0
    for item in items:
        print(item[0],"Rs",item[1])
        total_bill+=item[1]
    print('total number of items:',len(items))
    print("your total bill is :Rs",total_bill)
    print('all additional items:')
    for details,description in customer_details.items():
        print(details,':',description)
swiggy("Nithin","Swiggy One",
       ["burger",250],["fries",100],["coke",50],
        payment_mode="UPI",
        delivery_instrustion="Dont ring the bell")
