# WAP to to find the srting is Paliindrome without slicing

# WAP to encrypt a string

str1 = input("Enter a string")
str2 = ''
l = len(str1)
print(l)
for i in range(0,l):
    n = ord(str1[i]) +100
    str2 = str2 + chr(n)


print(f"Original String {str1}")
print(f"Encrypted String {str2}")

"""Take Phone Number of 10 digit and 2 Dashes, with dashes after area code  and three are the numbers
Eg. - 121-121-2121 is correct

Code - 
p = input(‘Enter Phone Number : ‘)
val = False
# length must be 12
if len(p) == 12 and p[3] == ‘-‘ and p[7] == ‘-‘:
if (p[:3]+p[4:7]+p[8:]).isdigit(): # all the characters except dashes should be digits
val = True

if val:
    print(p, ‘is valid’)
else:
    print(p, ‘is invalid’)

"""

"""
tup1 = ()
for i in range(0,401,2):
        tup1 = tup1 + (i**2,)


print(tup1)
"""
tup1 = ()
no_of_tupple = int(input("How many tuples you want in one nested tuple"))
count = 0
eventup= ()
for i in range(no_of_tupple):
    num1 = int(input("Enter the first number"))
    num2 = int(input("Enter the second number"))
    tup = (num1,num2)
    tup1 = tup1 + tup
    if num1%2== 0 and num2%2 == 0:
        count += 1
        eventup = eventup + (tup,) 
print("There are", count, "tupples having even numbers","\n",eventup)

"""WAP to input 2 tupples seq_a and seq_b and prints true if such that a and b are equal"""