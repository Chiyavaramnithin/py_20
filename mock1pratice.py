'''create a python application to develop simple hospital billing system design function like cal bill with *args charges of variable type
 or orbitary type and other apply insurance with **kwargs of variable or orbitary type  and create a function add taxes with keyword args
of variable type the program should accepts the multiple charges like consultant ,treatment apply insurance deduction and apply tax'''

hospital_bill=lambda*args:sum(args)
apply_insurance = lambda amount, **kwargs: amount - sum(kwargs.values())
total_taxes = lambda amount, **kwargs: amount + sum(kwargs.values())
total_bill=hospital_bill (10000,2000,3000)
print("total_bill",total_bill)
after_insurance=apply_insurance(total_bill,lic1=1000,lic2=1500,lic3=1800)
print("after_insurence",after_insurance)
after_taxes=total_taxes(after_insurance,gst1=500,gst2=300)
print("after_taxes",after_taxes)
'''Design a Python program for a supermarket billing system. Create a function  calculate_total(*prices) that accepts 
the prices of multiple items and returns their total cost. Then define a function apply_discount(*amount) that applies
 a 10% discount if the total exceeds 1500. Finally, create a function final_bill(**details) that accepts keyword 
 arguments such as amount, tax, and packing_charge, and returns the final payable bill. Display the final amount
  using a single nested function call.'''
calculate_total=lambda*prices:sum(prices)
apply_discount=lambda amount:amount-(amount*0.10) if amount>1500 else amount
final_bill=lambda **details:details['amount']+details.get('tax',0)+details.get('packing_charge',0)
total = calculate_total(500, 700, 600, 400)
print("Total before discount:", total)
discounted = apply_discount(total)
print("After discount:", discounted)
final = final_bill(amount=discounted, tax=100, packing_charge=50)
print("Final Payable Bill:", final)


