#Recursions: Recursive Vs Iterative Approach

#"Recursion occurs when a function calls itself."

"""Factorial method :-"""
#(n!) - It is the symbol of factorial
# n! = n * n-1 * n-2 * n-3.......1
# n! = n * (n-1)!
def factorial_iterative(n):
    """
        :param n: Integer
        :return: n * n-1 * n-2 * n-3.......1
    """
    fac = 1
    for i in range(n):# i will start from 0 aand gooes to n EX- if n=5 .then 0-5 It will not include 5
        fac = fac * (i + 1)#0 se multiplication prevent karne ke liye humnne plus 1 kiya
    return fac
"""
Calculation Explained-:
IF N = 5; Range = 0-5 means 0,1,2,3,4 ; i ki 5 values h
i will change into 0,1,2,3,4[Not 5]; 
fac = 1 * (0+1)=1
fac = 1 * (1+1)=2
fac = 2 * (2+1)=6
fac = 6 * (3+1)=24
fac = 24 * (4+1)=120(return Value)
"""



def factorial_recursive(n):
    """
        :param n: Integer
        :return: n * n-1 * n-2 * n-3.......1
    """
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)#It is recursion(using function inside a function)
#     # 5 * factorial_recursive(4)
#     # 5 * 4 * factorial_recursive(3)
#     # 5 * 4 * 3 * factorial_recursive(2)
#     # 5 * 4 * 3 * 2 * factorial_recursive(1)
#     # 5 * 4 * 3 * 2 * 1 = 120


# It is a fibonacci series-:
# 0 1 1 2 3 5 8 13
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


number = int(input("Enter then number"))
print("Factorial Using Iterative Method", factorial_iterative(number))
print("Factorial Using Recursive Method", factorial_recursive(number))
print(f"Fibonacci Number on index {number} is => ",fibonacci(number))

agg = 0

for i in range(1, number+1):
    agg = agg + i

print(f"Sum of numbers upto {number} is {agg}")

agg2 = 1

for i in range(1, number+1):
    agg2 = agg2 * i

print(f"Factorial of {number} is {agg2}")


""" A Program returning even number from  n to 0 inn reverse order"""
n = int(input("Enter the number"))
for i in range(n,0,-2):
    if n%2 != 0:
        n = n+1
        print(i)
    else:
        print(i)


str = input("Enter a string")

for i in str:
    print(i)