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
"""



