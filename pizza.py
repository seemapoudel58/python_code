#Based on user's order, work out their final bill.
#Small Pizza= Rs.15
#Medium Pizza= Rs.20
#Large Pizza= Rs.25
#Pepperoni for Small Pizza: +RS2
#Pepperoni for Medium or Large Pizza: +RS3
#Extra cheese for any size pizza: +RS1
print("Welcome to Pizza Deliveries!")
size = input("What is the size of the pizza you want? S, M, or L :\n")
add_pepperoni = input("Do you want to add pepperoni? Y or N:\n")
add_cheese = input("Do you want to add cheese? Y or N :\n")
bill = 0
if (size == "S"):
    bill += 15
elif (size == "M"):
    bill += 20
else:
    bill += 25

if (add_pepperoni == "Y"):
    if (size == "S"):
        bill += 2
    else:
        bill += 3

if (add_cheese == "Y"):
    bill += 1

print(f"Your Total bill is Rs {bill}.")
