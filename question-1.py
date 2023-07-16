# write a program that adds two digits in a 2 digitnumber. for example if the input was 45, then the output must me 4+5=9
number = input("enter the two digits:")
first_digit = number[0]
second_digit = number[1]
message = f"The sum is:{int(first_digit)+int(second_digit)} "
print(message)
