print("Welcome to Treasure Island!\nHere is the Map 👇🏻")
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
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
******************************************************************************* 
''')
print("Welcome to Treasure Island!\nHere is the Map 👆🏻 ")
print("Your Mission is to find the treasure!")

direction_1 = input("You're at a cross road. Where do you want to go? Type 'Left' or 'Right'\n")
lower_direction_1 = direction_1.lower()

if lower_direction_1 == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    wait_swim = input("Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
    lower_wait_swim = wait_swim.lower()
    if lower_wait_swim == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        doors = input("One red, one yellow and one blue. Which colour do you choose?\n")
        lower_doors = doors.lower()
        if lower_doors == "yellow":
            print("You found the treasure! You Win!")
        elif lower_doors == "red":
            print("It's a room full of fire. Game Over.")
        elif lower_doors == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("Wrong door entered. Game Over")
    elif lower_wait_swim == "swim":
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
