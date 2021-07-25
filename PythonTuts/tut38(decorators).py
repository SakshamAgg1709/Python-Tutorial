#Decorators in Python

# def function1():
#     print("Subscribe now")

# func2 = function1
# del function1#It is to delete the function1 but func2 will run as it is because it is a copy of function1
# func2()

def funcret(num):
    if num == 0:
        return print
    if num == 1:
        return int

a = funcret(1)
print(a)
b = funcret(0)
print(b)

def execution(func):
    func("this")

execution(print)

def dec1(func1):
    def nowexec():
        print("Executing NOw")
        func1()
        print("Executed")
    return nowexec()

@dec1# => it is same as "who_is_Saksham = dec1(who_is_Saksham)"
def who_is_Saksham():
    print("Saksham is a good boy")

# who_is_Saksham = dec1(who_is_Saksham)

who_is_Saksham()

