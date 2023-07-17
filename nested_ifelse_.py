# write a program that interprets the body mass index(bmi) based on a user's weight and height. It should tell them the interpretation of their bmi based on the bmi values.
# under 18.5 they are underweight
# over 18.5 but below 25 they have a normal weight
# over 25 but below 30 they are overweight
# over 30 but below 35 they are obese
# above 35 they are clinically obese.

weight = int(input("Enter your weight in kg:"))
height = float(input("Enter your height in meter:"))
bmi = round(weight/height**2)

if (bmi < 18.5):
    print(f"Your bmi is {bmi}, you are underweight.")
elif (bmi < 25):
    print(f"your bmi is {bmi}, you have a normal weight")
elif (bmi < 30):
    print(f"Your bmi is {bmi}, you are overweight. ")
elif (bmi < 35):
    print(f"Your bmi is {bmi}, you are obese.")
else:
    print(f"Your bmi is{bmi}, you are clinically obese.")
