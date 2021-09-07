"""to find Simple and Compound interest."""

"""
print("Please enter the follwing inputs, Please enter numbers  only ( PLease Avoid %,$,₹)")
p = float(input("Enter Principal Amount( Avoid $, ₹)"))
r = float(input("Enter Rate of Interest (Avoid %)"))
t = float(input("Enter Time in years"))

simple_interest = (p*r*t)/100
Amount = p * (pow((1 + r / 100), t))
CI = Amount - p
print("Simple Interest = ", simple_interest)
print("Compund Interest = ", CI)
"""
"""Write a Program to find  5 multiples of a given number.(without iteration statement)"""

"""
n = int(input("Enter number:\n"))
print("First five multiples of", n, "are")
print(n, n * 2, n * 3, n * 4, n * 5)
"""

"""to reverse the digits of a given three digit number. Eg. Input=345, output must be 543. (without iteration statement)"""

"""
inp1 = input("Enter a three digit number:\n")
print(inp1[::-1])
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
Square roots of quadratic equation
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


