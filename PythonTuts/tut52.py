# Diamond shape problem in Multiple Inheritance in Python

class A:
    def set(self):
        print("This is a method from class A")
    pass

class B(A):
    def set(self):
        print("This is a method from class B")
    pass

class C(A):
    def set(self):
        print("This is a method from class C")
    pass

class D(B,C):
    def set(self):
        print("This is a method from class D")
    pass

a = A()
b = B()
c = C()
d = D()

d.set() # Here we can see the confusion due to manysymbols of o in Pycharm on LHS of the classes
# But it will print thr set method of class D
"""In Python it is esy to figure out the problrem of multiple inheritance but in other programming languages it is not easy
Thatswhy it is adviced to programmer to not to use Multiple inheritance 
"""