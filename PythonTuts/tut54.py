# Abstract Base Class & @abstractmethod in Python

# from abc import ABCMeta , abstractmethod - It is for old version
from abc import ABC , abstractmethod #It will work simialry as above statement - Works in Version above 3.4

class Shape(ABC):#This syntax is for new version - For old version - Shape(metaclass = ABCMeta)
    @abstractmethod
    def printarea(self):# Ab ye method banana har class ke liye compulsory h jo bhi Shape class ko inherit karti h
        return 0



class Rectangle(Shape):
    type = "Rectangle"
    sides = 4

    def __init__(self):
        self.length = 5
        self.breadth = 7

    def printarea(self):
        return self.length * self.breadth

type1 = Shape()#It will pose an error beacuse you can not mae an object in the the abstract base class
rect1 = Rectangle()
print(rect1.printarea())