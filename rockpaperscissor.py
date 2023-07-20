# Rock-Paper-Scissors Game
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissor]
user_choice = int(input(
    "What do you choose? Type 0 for rock and 1 for paper and 2 for scissors\n"))
if (user_choice >= 3 or user_choice < 0):
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print(f"Computer choose:\n ")
    print(game_images[computer_choice])

    if (user_choice == 0 and computer_choice == 2):
        print("Yay! You Win.")
    elif (computer_choice == 0 and user_choice == 2):
        print("You lose!")
    elif (computer_choice > user_choice):
        print("Oops, You lose.")
    elif (user_choice > computer_choice):
        print("You Win!")
    elif (computer_choice == user_choice):
        print("Thats a draw.")
    else:
        print("You typed invalid number. You lose ")
