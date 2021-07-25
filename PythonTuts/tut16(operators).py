#Operators in Python

# Arithmetic Operators
# Assignment Operatorss
# Comparison Operators
# Logical Operators
# Identify Operators
# Membership Operators
# Bitwise Operators

"""Arithmetic Operators"""

print("2 + 3 =" ,2+3)
print("2 - 3 =" ,2-3)
print("2 * 3 =" ,2*3)
print("2 ** 3 =" ,2**3)
print("2 / 3 =" ,2/3)
print("2 // 3 =" ,2//3)#point ke baad jo bhi hoga print nhi hoga
print("2 % 3 =" ,2%3)#It will give the remainder only

print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tAssignment Operators")

x = 5
print(x)
x += 7 #5 mein 7 add ho gaya
print(x)
x-=4
print(x)
x%=7 # Again remainder(8/7)
print(x)

print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tComparison Operators")

i = 5
print(i == 5)
print(i != 5)
print(i >  5)
print(i >=  5)# 5 ke equal to h na i

print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tLogical Operators")
a = True
b = False

#'and' mein agar ek bhi false h to false return karega
print(a and b)
print(a and a)
print(b and b)
# 'or' mein agar ek bhi true h to true return karega
print(a or b)
print(a or a)
print(b or b)

print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tIdentity Operators")


print(3 is not 4)
print(3 is not 3)
print(a is b)# Yaha a and b upar se uthaya h (a =True , b= False)
print(b is not a)

print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tMembership Operators")

list = [12 , 23, 34, 44, 3, 499, 322, 3443,133, 1]
print(233 in list)# Simple question ans.
print(133 in list)

print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tBitwise Operators")

# #These are binary values
# 0 - 00
# 1 - 01
# 2 - 10
# 3 - 11
#And =&
#Or = |

print(0 & 1)# 00 and 01 = 00 - This is 0
print(0 | 1)# 00 or 01 = 01 - This is 1
print(0 | 3) #00 or 11 = 11 - This is 3
print(2 | 3)