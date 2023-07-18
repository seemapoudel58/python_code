print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
direction = input(
    "You're at a crossroad. Do you want to move left or right?:\n").lower()
if (direction == "left"):
    sw = input("You've come to a lake. Do you want to swim or wait?:\n").lower()
    if (sw == "wait"):
        door = input(
            "There is a house with 3 doors. Which door do you want to choose? red, blue, or yellow\n").lower()
        if (door == "yellow"):
            print("Congratulations! You Win.")
        elif (door == "red"):
            print(" You got attacked by a fire. Game over.")
        elif (door == "blue"):
            print("You got attacked by a beast. Game over.")
        else:
            print("You choose the room that doesnot exit. Game over.")

    else:
        print("You got attacked. Game over.")

else:
    print(" You fell into a hole. Game over.")
