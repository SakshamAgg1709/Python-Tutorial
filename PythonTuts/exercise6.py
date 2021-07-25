"""Snake Water Gun Game"""

import random



print("\t\t\t\t\t\t\t\t\t\t\t\t\tLet's start a Snake ,Water ,Gun Game")

t  = 0
c = 10
i = 0
j = 0
while( c>=1):

    user = input("Enter S for snake ,G for gun ,W for Water")
    user2 = user.capitalize()
    li = ["Snake", "Water", "Gun"]

    comp = random.choice(li)
    if (user2 == "S" and comp == "Snake") or (user2 == "W" and comp == "Water") or (user2 == "G" and comp == "Gun"):
        print("TIE")
        c = c - 1
        print("Number of chances left", c)
        t = t + 1
        continue

    elif (user2 == "S" and comp == "Gun") or (user2 == "G" and comp == "Water") or (user2 == "W" and comp == "Snake"):

        print("Computer WON ")
        # print("Number of chances left", c)
        c = c - 1
        print("Number of chances left", c)
        j = j + 1
        continue



    elif (user2 == "S" and comp == "Water") or (user2 == "G" and comp == "Snake") or (user2 == "W" and comp == "Gun"):

        print("You WON")
        c = c - 1
        print("Number of chances left", c)
        i = i + 1
        continue


    else:
        print("Enter correct input")
        # print("Number of chances left", c)
        continue


print("Computer Won " , j ," times" , "\nYou won" ,i ,"times" , "\nTIE = " ,t ,"times")

if j > i:
    print("Computer won this GAME")
elif i > j:
    print("You won this GAME")
elif i == j:
    print("The Game is TIE")

