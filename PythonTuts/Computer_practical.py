"""to find Simple and Compound interest."""


# print("Please enter the follwing inputs, Please enter numbers  only ( PLease Avoid %,$,₹)")
# p = float(input("Enter Principal Amount( Avoid $, ₹)"))
# r = float(input("Enter Rate of Interest (Avoid %)"))
# t = float(input("Enter Time in years"))

# simple_interest = (p*r*t)/100
# Amount = p *((1 + r / 100)** t)
# CI = Amount - p
# print("Simple Interest = ", simple_interest)
# print("Compund Interest = ", CI)

"""Write a Program to find  5 multiples of a given number.(without iteration statement)"""

"""
n = int(input("Enter number:\n"))
print("First five multiples of", n, "are")
print(n, n * 2, n * 3, n * 4, n * 5)
"""

"""to reverse the digits of a given three digit number. Eg. Input=345, output must be 543. (without iteration statement)"""
"""
n=int(input("Enter any 3 digit number \n"))
r=0
if n<1000 and n>99:
    while (n>0):
        rem=n%10
        r=r*10+rem
        n=n//10
    print("\nThe reversed number is ",r)

else:
    print("\n!Enter Input Correctly!")

"""

""" To convert numbers into words"""

"""

ones = ('Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine')

twos = ('Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen')

tens = ('Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety', 'Hundred')

suffixes = ('', 'Thousand', 'Million', 'Billion')


def process(number, index):
    if number == '0':
        return 'Zero'

    length = len(number)

    if (length > 3):
        return False

    number = number.zfill(3)
    words = ''

    hdigit = int(number[0])
    tdigit = int(number[1])
    odigit = int(number[2])

    words += '' if number[0] == '0' else ones[hdigit]
    words += ' Hundred ' if not words == '' else ''

    if (tdigit > 1):
        words += tens[tdigit - 2]
        words += ' '
        words += ones[odigit]

    elif (tdigit == 1):
        words += twos[(int(tdigit + odigit) % 10) - 1]

    elif (tdigit == 0):
        words += ones[odigit]

    if (words.endswith('Zero')):
        words = words[:-len('Zero')]
    else:
        words += ' '

    if (not len(words) == 0):
        words += suffixes[index]

    return words;

def getWords(number):
    length = len(str(number))

    if length > 12:
        return 'This program supports upto 12 digit numbers.'

    count = length // 3 if length % 3 == 0 else length // 3 + 1
    copy = count
    words = []

    for i in range(length - 1, -1, -3):
        words.append(process(str(number)[0 if i - 2 < 0 else i - 2: i + 1], copy - count))
        count -= 1;

    final_words = ''
    for s in reversed(words):
        temp = s + ' '
        final_words += temp

    return final_words
# End Main Logic
# Reading number from user
number = int(input('Enter any number: '))

print('%d in words is: %s' %(number, getWords(number)))
"""

"""
x = int(input("Enter any num from 0-10\n->"))
if x == 0:
    print(x, '=> Zero')

elif x == 1:
    print(x, '=> One')

elif x == 2:
    print(x, '=> Two')

elif x == 3:
    print(x, '=> Three')

elif x == 4:
    print(x, '=> Four')

elif x == 5:
    print(x, '=> Five')

elif x == 6:
    print(x, '=> Six')

elif x == 7:
    print(x, '=> Seven')

elif x == 8:
    print(x, '=> Eight')

elif x == 9:
    print(x, '=> Nine')

elif x == 10:
    print(x, '=> Ten')

else:
    print('Enter Input Correctly')
"""
"""
Square roots of quadratic equation
"""

"""
print("Enter the coefficients of quadratic equation:")

a = int(input("Enter the coefficient of x2:\n"))
b = int(input("Enter the coefficient of x:\n"))
c = int(input("Enter the constant term:\n"))

d = (b**2)- (4*a*c)


if d == 0:
    r1 = (-b)/2*a
    r2 = (-b)/2*a
elif d > 0 :
    d_sqr = d ** .5
    r1 = ((-b) + d_sqr)/2*a
    r2 = ((-b) - d_sqr)/2*a
elif d <0 :
    print("There are no real roots")

print("Square roots of the equation are", "\n", r1,"\n", r2)

"""
""" Find the highest number"""

highest = 0

while True:
    inp = int(input("Enter any number:\n"))

    if inp >highest:
        highest = inp
    elif inp == 0:
        print("The Highest number you entered is ", highest)
        break
    else:
        continue

"""Write a program that takes string with multiple words and then capitalize the first letter of each word and forms a new string out of it."""
"""
str = input("Enter any string with more than one word:\n")
string = str.title()

print(string)
"""

"""Sum of 10 integers"""

"""
print("Enter any 10 numbers which you want to add")
sum = 0

for i in range(10):
    num1 = int(input("Enter the number:\n"))
    sum+= num1

print("The Sum of entered numbers =>", sum )
"""

"""Find the highest and the second highest number among four numbers"""

"""
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))
largest = 0
sec_largest = 0

if (num1 >= num2) and (num1 >= num3)and (num1 >= num4):
   largest = num1
   if num2 >= num3 and num2 >= num4:
       sec_largest = num2
   elif num3 >= num2 and num3 >= num4:
       sec_largest = num3
   elif num4 >= num2 and num4 >= num3:
       sec_largest = num4

elif (num2 >= num1) and (num2 >= num3)and (num2 >= num4):
   largest = num2
   if num1 >= num3 and num1 >= num4:
       sec_largest = num1
   elif num3 >= num1 and num3 >= num4:
       sec_largest = num3
   else:
       sec_largest = num4

elif (num3 >= num1) and (num3 >= num2) and (num3 >= num4):
   largest = num3
   if num1 >= num2 and num1 >= num4:
       sec_largest = num1
   elif num4 >= num1 and num4 >= num2:
       sec_largest = num4
   else:
       sec_largest = num2

else:
   largest = num4
   if num1 >= num2 and num1 >= num3:
       sec_largest = num1
   elif num2 >= num1 and num2 >= num3:
       sec_largest = num2
   else:
       sec_largest = num3


print("The Highest Number is", int(largest), "\n","The Second Highest Number is ", sec_largest)

"""
"""
str1=input("Enter any word you want to check \n")
if str1==str1[::-1]:
    print("Yes",str1,"is a Palindrome ")
else:
    print("No",str1,"is not a Palindrome")
"""
"""

# For finding prime numbers in a specified range
m = int(input("Enter lower range: "))
n = int(input("Enter upper range: "))
print("Required prime numbers: ")

for num in range(m, n + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
"""
"""
#FIBONACCI SERIES

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

if nterms <= 0:
   print("Please enter a positive integer")

elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1, end=" ")
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
"""
"""

# Even or Odd in a range
n = int(input("Enter last value of range starting from 1 to ->"))
c = int(input("Enter your the number from 1 to 3 in accordane to your choice:\n1 for Even\n2 for Odd\n3 for Exit the Program:\n"))
for i in range(1, n + 1):
    a = i % 2
    if c == 1:
        if a == 0:
            print(i, "is even number")

    elif c == 2:
        if a != 0:
            print(i, "is odd number")

    elif c == 3:
        print("Program Ended")
        break
"""
"""
#Profit / Loss Decider
total_cp= 0
total_sp= 0


for i in range(1,11):
    print("Item",i,"\n")
    cost_price = float(input("Enter cost price -> "))
    sell_price = float(input("Enter selling price -> "))
    total_cp += cost_price
    total_sp += sell_price

if total_cp > total_sp :
    print("\nLoss Occurred :(")
elif total_cp == total_sp :
    print("\nNo Loss, No Profit :|")
else :
    print("\nProfit Occurred :)")
"""

"""

# Number Palindrome
num =int(input("Enter number\n"))
num2 =num
reverse=0
while(num>0):
    dig=num%10
    reverse=reverse*10+dig
    num=num//10
if(num2==reverse):
    print("The number is a PALINDROME.")
else:
    print("The number is NOT a PALINDROME.")
"""
""" 

str=input("Enter string \n")

count_upper = 0
count_lower = 0
count_alpha = 0
count_digit = 0

for i in range(len(str)):
    if(str[i].isalpha()):
        count_alpha = count_alpha + 1
    elif(str[i].isdigit()):
        count_digit = count_digit + 1
    else:
        continue

for n in str:
    if n.islower():
        count_lower = count_lower + 1
    elif n.isupper():
        count_upper = count_upper + 1
    else:
        continue

print("\nTotal Number of Alphabets in this String :  ", count_alpha)
print("Total Number of Digits in this String : ", count_digit)
print("Total Number of Lowercase Characters in this String : ",count_lower)
print("Total Number of Uppercase Characters in this String : ",count_upper)
"""

"""
str1 =input("Enter any word  \n")
if str1 == str1[::-1]:
    print("Yes",str1,"is a Palindrome String")
else:
    print("No",str1,"is NOT a Palindrome String")

inp = int(input("Enter any number\n"))
sum = 0
while (inp > 0):
    rem = inp % 10
    sum = sum + rem
    inp = inp // 10

print("\nSum of the digits of entered number is ->  ", sum)

"""
#
# a = True
# b = False
# print(a or b)
# print(a and b)
# str = "Hard work pays off"
#
# print(str[2])
# print(str[-3])
# print(str[2:5])
# print(str[2:5:2])
#
# print( (1.1 + 2.2) == 3.3 )

# a,b,c,d = 9.2,4,2,12
# print(c//b)
# print(a/4)
# print(b**2)
# print(d%c)
# for x in range(1,4):
#     for y in range(2,5):
#         if x * y > 10 :
#             break
#         print(x*y)