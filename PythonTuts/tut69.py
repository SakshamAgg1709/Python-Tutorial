# Raising exeptions in Python

# a = input("What is your name?")
#
# # if a.isnumeric():
# #     pass
# # # Let here be so many lines of codes that take 1 hour to run
#
# """if the number is not numeric our time is wasted, to avoid this we have the following code"""
#
# if a.isnumeric():
#     raise Exception("Numbers are not allowedd")
#
# print(f"hello{a}")
#
# """THere are some Built in Exceptions in Python"""
#
# b = input("How much do u earn?")
#
# if int(b) == 0:
#     raise ZeroDivisionError("b is 0 so stopping the program")

c = input("Enter your name")
try:
    print(f)

except Exception as e:
    if c=="harry":
        raise ValueError("Harry is blocked, he is not allowed")

    print("Exceeption Handeled")# Iss case mein Do error display hoga



"""Task"""


li = [ "harry", "Skasham"]
print(li)
inp = int(input("Enter any index you want to print"))

if inp >= 2:
    raise IndexError("Your entered index is out of range")
else:
    print(li[inp])


a = int(input("Enter a"))
b = int(input("Enter b"))
c = a**b

if len(str(c)) > 10:
    raise OverflowError("The result is out of range")
else:
    print(c)