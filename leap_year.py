# day 3
# write a program that works out whether if a given year is a leap year. A normal year has a 365 days, leap year hve 366, with an extra day in february.

year = int(input("Enter the year:"))
if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print("It is a leap year.")
        else:
            print("It is not a leap year.")
    else:
        print("It is a leap year.")
else:
    print(" It is not a leap year.")
