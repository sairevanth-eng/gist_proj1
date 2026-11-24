'''has_ticket = True
age=18
if has_ticket and age>=18:
    print("You can enter the movie")
else:
    print("Entry denied")
    
has_ticket = False
age=18
if has_ticket and age>=18:
    print("You can enter the movie")
else:
    print("Entry denied")
    
    
actual_price = 50
money_with_you=40
if money_with_you>=actual_price:
    print("You can eat samosa")
else:
    print("you cannot eat samosa")
    
actual_price = 50
money_with_you=int(input("Enter money you have: "))
if money_with_you>=actual_price:
    print("You can eat samosa")
else:
    print("you cannot eat samosa")
    
actual_price = 50
quantity=int(input("Enter quantity"))
total_price=actual_price*quantity
print(total_price)

marks = 85
income = 1500000
if marks >= 90 or income >200000:
    print(" Eligible for scholarship")
else:
    print("Not eligible")
    
isclosed = False
if not isclosed:
    print("Restaurant is open")
else:
    print("Restaurant is closed")'''
    
money_with_you=int(input("Enter money you have: "))
if money_with_you>=50:
    print("You can eat samosa(or)puff(or)ice cream")
elif money_with_you>=30:
    print("You can eat puff(or)ice cream")
elif money_with_you>=20:
    print("You can eat ice cream")
else:
    print("You cannot eat anything")