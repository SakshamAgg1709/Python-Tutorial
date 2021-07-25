#Object Oriented Programming in Python
"""
 Classes  - Template
 Object - Instance of the class
 Principle of OOPs is : DRY - Do Not Repeat yourself
"""

# Our first Class in Python:-

class Student:
    pass#Agar main chahta hu ki abhi kucch na ho to main Pass likh sakta hu; error throw nhi karega

harry  = Student()
Saksham = Student()

harry.name = "Harry"
harry.std = 12
harry.section = 1
Saksham.std = 11
Saksham.subjects = ["English" , "Accountacy" ,"Business Studies" , "Economics" , "Computer Science"]

print(harry , Saksham)
print(harry.std)
print(harry.section)
print(harry.name , Saksham.std)
print(Saksham.subjects)