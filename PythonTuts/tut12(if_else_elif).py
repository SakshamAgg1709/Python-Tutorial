#If-Else & Elif Conditionals in Python

# var1 = 3
# var2 = 34
#
# var3 = int(input())

# if var3>var2:
#     print("Greater")#Here indentation is very important
# if var3==var2:
#     print("Equal")
#
# else:
#     print("Lesser")
#
# if var3>var2:
#     print("Greater")#Here indentation is very important
# elif var3==var2:#ELif is used so that python stops  checking the further "if" statements if the first one is true
#     print("Equal")
#
# else:
#     print("Lesser")

list = [5,6,7]

if 5 in list:
    print("Yes it is in the list")
else:
    print("No 5 is not in the list")

if 6 not in list:
    print("6 is not in the list ")
else:
    print("6 is in the list")



"""Quiz"""

print("Enter your age(4-80)")
age = int(input())#It is most imp. because input function will give you a string value

# THIS IS A LONG METHOD ,DON'T USE THIS
# if 4>inp:
#     print("Enter your correct age")
# elif inp>80:
#     print("Enter  your correct age")
#
# elif inp>18:
#     print("You can drive")
# elif inp==18:
#     print("You should apply for driving lisence")
# elif inp<18:
#     print("You cannot drive")

#USE THIS METHOD

if age<=4 or age>80:
    print("Enter your correct age")
elif age>18:
         print("You can drive")
elif age==18:
         print("You should apply for driving lisence")
elif age<18:
         print("You cannot drive")









