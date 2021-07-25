# A Program to find that a number entered by the User is prime or nit


inp = int(input("Enter a number:\n"))

if inp > 1:
    for i in range(2,inp):#Yaha 1 se nhi lenge kyuki 1 se to har number hi divisible h
        if inp % i == 0:# IT means the remainder is 0
            print(inp , "is composite number")
            break
    else:#Here we have used else for 'for-statement' not for 'if' because otherwise it will print 'prime' multiple times
        print(inp, " is a prime number")




elif inp == 1:
    print("1 is a unique number")
else:
    print("Enter CORRECT input")




"""Another Practise problem"""

"""One Line Solution"""

a = print([f"{i+1}" for i in range(int(input("Enter the number")))])

