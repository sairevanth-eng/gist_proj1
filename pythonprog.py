item="Fried rice"#string
price=40 #integer
rating=4.5 #float
is_veg=True #boolean
#print(type(price))
#print(type(rating))
#print(type(is_veg))
#print(type(item))
print("Welcome to campus canteen")
menu=["Fried rice","Noodles","idli","samosa"]
print(type(menu))
print("Menu items are: ",menu)
print(menu[0])
print(menu[1])
print(menu[2])
print(menu[3])
print("dosa appended")
print(menu)
menu.append("Dosa")
print("menu changed using indexing")
menu[1]="egg noodles"
print(menu)
print(item,"cost = ",price)
working_days=("Monday","Tuesday","Wednesday","Thursday","Friday")
print("Working days are: ",working_days)
#print(working_days[4])

prices = {
"Fried rice": 40,
"Noodles": 30,
"idli": 20,
"samosa": 10

}