# F -string and String functions in Python

#F - String

me = "Saksham"
a = "This is %s"%me # By this we can add Another string to anothor

me = "Saksham"
a1 = 3
# a=  "This is %s %s"%(me, al)#Jitne zyada str. h ya int. h utne "%s" lagane h
# a = "This is {} {}"
# a = "This is {1} {0}"#By this  we can change the order of string and integer
b = a.format( me , a1)#This is another way to add string and integer
print(b)

"""Beter way"""

"""This is F-String"""
#f-string is Fast String :)
import math

a2 = f"This is {me} {a1} {4*12} {math.cos(90)}"
print(a2)

