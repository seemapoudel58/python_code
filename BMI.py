# write a program that calculates the body mass index(BMI)from a user's weight and height.

weight = input("Enter your body weight in kg:")
height = input("Enter your height in meter:")
BMI = int(weight)/float(height)**2
new_BMI = int(BMI)
message = f"The BMI of your body is :{new_BMI}"
print(message)
