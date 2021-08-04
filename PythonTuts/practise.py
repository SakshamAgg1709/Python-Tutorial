# # A Program to find that a number entered by the User is prime or nit
#
#
# inp = int(input("Enter a number:\n"))
#
# if inp > 1:
#     for i in range(2,inp):#Yaha 1 se nhi lenge kyuki 1 se to har number hi divisible h
#         if inp % i == 0:# IT means the remainder is 0
#             print(inp , "is composite number")
#             break
#     else:#Here we have used else for 'for-statement' not for 'if' because otherwise it will print 'prime' multiple times
#         print(inp, " is a prime number")
#
#
#
#
# elif inp == 1:
#     print("1 is a unique number")
# else:
#     print("Enter CORRECT input")
#
#
#
#
# """Another Practise problem"""
#
# """One Line Solution"""
#
# a = print([f"{i+1}" for i in range(int(input("Enter the number")))])
#
#
# """
# m = int(input("Enter the value of m"))
# n = int(input("Enter the value of n"))
#
# for i in  range(m, n+1):
#     if i%m == 0:
#         print(i)
#     else:
#         print("THer is no number divisible by 5 in this range")
#
# if m>n:
#     print("Enter value of n greater than m")
# """
#
# # Python program to check if the number is an Armstrong number or not
#
# # take input from the user
# num = int(input("Enter a number: "))
#
# # initialize sum
# sum = 0
#
# # find the sum of the cube of each digit
# temp = num
# while temp > 0:
#    digit = temp % 10
#    sum += digit ** 3
#    temp //= 10
#
# # display the result
# if num == sum:
#    print(num,"is an Armstrong number")
# else:
#    print(num,"is not an Armstrong number")
# #
# # """Tell howwmany rpime numbers are therre in na reange"""
# min = int(input("Enter the minimm value"))
# max = int(input("Enter the maximum value"))
#
# c = 0
#
# for i in range(min, max+1):
#     if i > 1:
#         for i in range(2 ,i):
#             if i % i ==0:
#                 break
#         else:
#             print(i)
#             c+=1
#
# print(f"There are {c} prime numbers in this branch")

a = float(input("Enter the length of First dide of triangle"))
b = float(input("Enter the length of Second dide of triangle"))
c = float(input("Enter the length of Third dide of triangle"))


if (a+b)<=c or (b+c)<=a or (a+c)<=b:
    print("The triangle is not possible")
else:
    if a == b == c:
        print("It is a Equilateral Triangle")
    elif a == b or b==c or a==c:
        print("It is a isoceles triangle")

    elif a!=b!=c:
        print("it is a scalene")




