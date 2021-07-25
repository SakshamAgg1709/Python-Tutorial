#Functions in Python


"""Built in Functions"""
# a = 3
# b = 5
# c = sum((a,b))
# print(c)

"""User defined Functions"""

def fun1():
    print("Hello you are in fun1")

print(fun1())# Yaha return function nhi h isliye 'none' display hoga
fun1()
fun1()
fun1()
fun1()

#docstring is mentioned in this function2

def function2(a,b):
    """This is function which will calculate average of two numbers
    This function doesn't work for three numbers"""
    average = (a + b)/2
    # print(average)
    return(average)

v = function2(5,7)

print(v)
print(function2.__doc__)