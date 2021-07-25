# Operator Overloading & Dunder in Python

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

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary/other.salary
    """THere are many methods like this , you can get more methods on Google - Mapping Operators in Python"""
    def __repr__(self):
        return f"Employee('{self.name}' , {self.salary} , '{self.role}')"

    def __str__(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"





emp1 = Employee("Harry" , 33 , "Programmer")
emp2 = Employee("Saksham" , 93 , "Jr. Programmer")
print(emp1 + emp2) # Yaha pe error ho jaaeyga untill we add a __add__ method
print(emp1/emp2)# Yaha par trudiv method use hua h untill we use repr or str
print(emp1)# It gives a very confusing statement- <__main__.Employee object at 0x0308B160>
"""
repr aur str ek jaise hi h but str ko jyada importance di jaati h 
print(emp1) - str method wlai string print hogi - reps method ko ignore kiya jaaeyga
print(repr(emp1)) - repr string -agar repr nhi h too str string print hogi
print(str(emp1)) - str string - agar str nhi h to repr string print hogi

"""