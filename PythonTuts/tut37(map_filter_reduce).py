#Map ,Filter and Reduce

numbers = ["3" , "4" , "34"]
#We want to convert nthe numbers in string into integers

"""Using For loop"""
# for i in range(len(numbers)):#We have used len or length to get integer values for range as numbers has only string values
#     numbers[i] = int(numbers[i])
#but it is not a god practise to use for loop again and again if it can be done using a single line

"""Using Map functionss"""
# print(map(int , numbers))#It returns a object
# numbers = list(map(int , numbers))#It will convert all items of the list into int() and typecaste them again in the list
#
# numbers[2] = numbers[2] + 1
# # print(numbers[2])
#
# num = [2,34,4,56,43,2]

#It is a new function
# def sq(a):
#     return a*a
"""We have made a lambda to replace this function"""


# square = list(map(lambda x:x*x , num))#It will return the square values of all the numbers in the list
# print(square)


def square(a):
    return a * a

def cube(a):
    return a*a*a

func = [ square ,cube]
num = [2,3,42,45,1,44,1,22]
#
"""Dhyan se samjhna phir samajh aa jaaeyga"""
for i in range(5):#It is normal range 0 ,1 ,2 ,3 ,4
    val = list(map(lambda x:x(i) ,func))#Yaha x ek baar square() aur ek baar cube() hoga
    print(val)

"""Filter Function"""
list_1 = [1,2,3,4,5,6,7,8,9]

def is_greater_5(num):
    return num > 5#Agar number greater than 5 h to ye true return karega nhi to false return karega

gr_than_5 =list(filter(is_greater_5 ,list_1))#Ye sirf true conditions return karega i.e. 6,7,8,9
#Sabse pehle check karega ki kaun si condition true h konsi false  ,uske baad sirf true wali return kar dega
# print(gr_than_5)

"""Reduce function"""

from functools import reduce

list_2 = [1,2,3,4]
#Now we want to add 1+2+3+4

"""Using For loop"""
# num =0
# for i in list_2:
#     num = num + i
# print(num)

"""Using reduce and a short one liner"""

num =reduce(lambda x,y:x+y ,list_2)#It will return 1+2+3+4
num =reduce(lambda x,y:x+y ,list_2)#It will return 1*2*3*4
print(num)