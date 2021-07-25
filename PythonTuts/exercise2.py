# Exercise 2 - Faulty Calculator
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result


print("Enter the first number")
num1 = int(input())
print("Enter the second number")
num2 = int(input())
print("Which operator you want to use(+ ,- ,*, /")
op = input()

if num1==45 and num2==3 and op=="*":
    print(555)
elif num1==56 and num2==9 and op=="+":
    print(77)
elif num1==56 and num2==6 and op=="/":
    print(4)
elif op== "+":
    print("Result => " , num1 + num2)
elif op== "-":
    print("Result => " , num1 - num2)
elif op== "*":
    print("Result => " , num1*num2)
elif op== "/":
    a =(num1/num2)
    print(format(a , ".2f"))#it is to restrict Decimal to only 2 decimal places
else:
    print("ERROR !!!! ,Please check your input")

