#*args and **kwargs in Python

# def function_name_print(a,b,c):
#     print(a,b,c)
#
# function_name_print("Harry" ,"Saksham" ,"Rohan")#It is easy to work BUT....

# What to do if we want to add more names; One method is to add 'd' and 'e' in the function and 2 names in the calling
# but is very diffucult to use if we want to add so many names
"""
def funargs(*args):#Star is very important=
    print(type(args))#It is a tuple as you can see
    print(args[0:])
"""


# We have to use normal argument always efore *args otherwise it will show error even if you change the position of
# arguments at the calling of the functionb
def funargs(normal , *args):#We can also write (normal , *argsrohan) or any other name after *args
    print(normal)
    for item in args:
        print(item)


#**kwargs ko hum **kwargssaksham bhi likh sakte h aur kuch bhi likh sakte h
def funargs(normal , *args , **kwargs):#It will also work similarly
    print(normal)
    for item in args:
        print(item)
    print("\nNow I would like to introduce sme of our heroes")
    for key,value in kwargs.items():#It is the syntax to use for loop in a dictionary
        print(f"{key} is a {value}")


normal = "I am a normal arguments and the Students are:-"
sa = ["Harry" ,"Saksham" ,"Rohan" , "Tanishka", "Vishesh" ]
kw = {"HArry":"Programmer" , "Saksham" : "Student" ,"Tanishka" : "Student" ,"Rohan":"Cook"}
funargs( normal ,*sa ,**kw)#List ke saare items function mein call ho gaye

