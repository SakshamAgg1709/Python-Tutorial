# Public , Private and Protected Access Specifiers in Python

"""
public - Everybody can use
private - Only I can use
protected - Only few selected ones can use
"""


class Employee:
    no_of_leaves  = 8# It is a public variable
    var = 9
    _protect  = 20 # It is a protected variable - It can be used only in the child classes or inherited classes
    __private = 300# It is a private variable but you can't use it like this - emp.__private
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


emp = Employee.from_str( "Saksham-10000000-Programmer")
print(emp._protect)
#print(emp.__private)#It will through an error due to name angling in Python
print(emp._Employee__private) # By this we can use a private variable

class Protected(Employee):
    pass

emp2 = Protected("Rohan" ,440  ,"Student")

print(emp2._protect)# Here we can use a protected variable
print(emp2._Employee__private)