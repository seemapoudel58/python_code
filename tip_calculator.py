# Tip calculator
print("Welcome to the tip calculator!")
Bill = float(input("What was the total bill?: Rs."))
tip = float(
    input("What percentage of tip you wouls like to give? 10, 12 or 20 :"))
people = int(input("How many people to split the bill?"))
Total_bill = int(Bill + tip/100*Bill)
message = f"Each person should pay Rs.{Total_bill/people}"
print(message)
