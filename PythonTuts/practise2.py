def palindrome(inp):
    if inp.isalpha() == True:
        if inp == inp[::-1]:
            print("It is a palindrome string")

        else:
            print("It is not a palindrome string")

    elif inp.isnumeric() == True:
        if int(inp) == int(inp[::-1]):
            print("It is a palindrome number")

        else:
            print("It is not a palindrome number")
    else:
        print("Pleaae enter either a string or a number")

inp = input("Please enter a input and Press enter:\n")
# print(type(inp))
palindrome(inp)

a = True
b = False
c = False


print(a and  b and c)