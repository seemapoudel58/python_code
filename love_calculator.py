print("Welcome to a love calculator!")
n1 = input("Enter the First Person name:")
n2 = input("Enter the Second Person name:")
nam = n1+n2
name = nam.lower()

t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")
true = t + r + u + e

l = name.count("l")
o = name.count("o")
v = name.count("v")
e = name.count("e")

love = l+o+v+e

true_love = int(str(true) + str(love))


if ((true_love < 10) or (true_love > 90)):
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif ((true_love <= 40) and (true_love >= 50)):
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}.")
