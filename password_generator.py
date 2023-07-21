# day-5 project
# password generator
import random

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*',
           '(', ')', '+', '-', '=', '[', ']', '{', '}', ';', ':', ',', '.', '/', '<', '>', '?', '|', '`', '~']
print("Welcome to a password generator!")
n_letters = int(input("How many letters do you want in your password?\n"))
n_symbols = int(input("How many symbols do you want in  your password?\n"))
n_numbers = int(input("How many numbers do you want in your password?\n"))

password_list = []
for char in range(1, n_letters+1):
    password_list += (random.choice(letters))

for char in range(1, n_symbols+1):
    password_list += random.choice(symbols)

for char in range(1, n_numbers+1):
    password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is : {password}.")
