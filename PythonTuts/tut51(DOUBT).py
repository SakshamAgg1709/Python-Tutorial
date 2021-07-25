# Overriding and Super() in Python

# class A:
#     classvar1 = "I am a class variable in Class A"
#
#     def __init__(self):
#         self.var1 = "I aminside class A's constructor"
#         self.classvar1 = "Instance var in class A"
#
# class B(A):
#     classvar1 = "I am a class variable in Class B"
#     pass
# a = A()
# b = B()

# print(b.classvar1) # Sabse pehle wo instance variable khojega jo init funcction ke andar h , waaha nhi mila to Class B mein class variable khojega , waha bhi nhi mila to wwo class A ke andar koi class variable khojega

"""FIRST REFER THE ABOVE PROGRAMM AND ITS COMMENT """

class A:
    classvar1 = "I am a class variable in Class A"

    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"
        self.special = "Special"

class B(A):
    classvar1 = "I am a class variable in Class B"
    def __init__(self):
        #super().__init__()#super class(inherited class) ke contructor ko run kar do
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instance var in class B"
        super().__init__()
        """DOUBT"""
        print(super().classvar1)# Isme dono classvar1 kyu print huye?
    pass

a = A()
b = B()

print(b.classvar1)# AB wo B class ke init function ke andar wale instance variable ko lega
"""But we want a special variable that is present only in Init function of CLass A"""

print(b.special)# It will throw error untill we add super function becaause we have overwrite the constructor of class B
print(b.var1 , b.classvar1)# Agar super function class B ke init ke niche h to Class A ke contructor ko maana jaeyga nhi to class B ke constructor ko maana jaaeyga