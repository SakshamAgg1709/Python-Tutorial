#Make the user to guess a number

print("You entered a  \"Number Guessing Game\" ")

n = 12
g = 10

print("Number of guesses", g)
while(True):#You can also use "for n in range(1-10):"

    inp =int(input("Guess a number:"))
    if inp == n :
        print("You won in " ,10  -  g ,"guesses")
        print("Congo")
        break

    elif g == 1:
        print("Sorry all guesses finished")
        print("GAME OVER")
        break

    elif inp > n:
        g = g- 1
        print("guess a lesser one")
        print("Number of guesses left" , g)
        continue
    elif inp < n:
        g  = g-1
        print("Go high")
        print(" Number of guesses left" , g)
        continue



