# Abstraction and Encapsulation in Python

# Encapsulation = Hiding the funcioning of a program  - Hiding the implementation from another program

"""
There is no extra code in this only undderstanding the concepts from the video
"""

class Employee:
    no_of_leaves  = 8
    def __init__(self , aname ,asalary , arole):
        self.name = aname
        self.salary  = asalary
        self.role  = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls , newleaves):
        cls.no_of_leaves = newleaves


    @classmethod
    def from_str(cls , string):
        return cls(*string.split("-"))


    @staticmethod
    def printgood(string):
        print("This is good" + string)


harry = Employee("Harry" , 5000000000  , "Instructor")
saksham = Employee("Saksham" , 100000000000000000 , "Student")
karan = Employee("Karan" , 100000 , "Junior Student")

