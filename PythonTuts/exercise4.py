# Exercise 4
# Pattern Printing
# Input = Integer n
# Boolean = True or False
#
# True n=5
# *
# **
# ***
# ****
#
# False n=5
# ****
# ***
# **
# *
# print("Pattern printing")
# num = int(input("Enter num how many rows you want : "))
# print("Enter 1 or 0")
# bool_val = input("1 for True value or 0 for False : ")
# if bool_val=="1":
#     for i in range(0,num+1):#If num =5 it will print between 0 and (5+1) i.e. 1,2,3,4,5
#         print("*"*i)
#
# elif bool_val == "0":
#     for i in range(num,0,-1):
#         print("*" * i)
#
# else:
#     print("ERROR")

print("Print Your Own STAR PATTERN"  )
print("For False:" , "\n* * * \n* * \n*" ,"\nFor True:" , "\n*\n* *\n* * *" )
n = int(input("Enter the no. of rows:"))
m = bool(int(input("Enter 0(False) or 1(True):")))

def star(n , m):
    if m == True:
        a = 1
        while(a<=n):
            print(a * "*")
            a = a + 1
    else:
        a = n
        while(a > 0):
            print( a * "*")
            a =  a - 1


star(n , m)

