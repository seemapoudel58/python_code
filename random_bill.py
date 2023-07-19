# Write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
import random
names = input("Give me everybody's name separated by comma:\n")
name = names.split(",")
# get the total number of items in length.
item = len(name)
chosen = random.randint(0, item-1)
person_name = name[chosen]
print(f"The person who is going to pay the bill is {person_name}.")
