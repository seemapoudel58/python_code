# create a program using maths and f string that tells us how many days, weeks, months we have left if we live until 90 years old
age = input("Enter your current age: ")
remaining_age = 90 - int(age)
remaining_months = remaining_age*12
remaining_weeks = remaining_age*52
remaining_days = remaining_age*365
message = f" You have {remaining_months}months, {remaining_weeks}weeks and {remaining_days}days left to live"
print(message)
