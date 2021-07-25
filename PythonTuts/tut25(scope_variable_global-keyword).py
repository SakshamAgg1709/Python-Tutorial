#Scope and Global Variables and Global Keyword in Python

l = 10 #Global Variable

def function1(n):
    l = 5#Local Variable
    m = 8#Local Variable
    print(l,m)#first it will refer the local variable

    print(n , "I have printed")


function1("This is me")
print(l)
#print(m) - It will through error as m is not a global  varialble

def function2(n):

    m = 8

   # l = l + 45 #you cannot change a global variable
    global l
    l = l + 4#Now you have permission to use a global variable
    print(l,m)


# x = 89# Global variable
#
# def harry():
#     x = 20
#     def rohan():
#         global x
#         x = 88#It is the last line of rohan() function
#     rohan()# iss function ne global variable x=39 ki value change ki h na ki local variable ki
#     print("After calling rohan()" ,"x = " , x)# Yaha local variable x = 20 print hoga
#
# harry()
# print(x)# Global variable 89 change hokar 88 hogaya due to the working of rohan() in harry()