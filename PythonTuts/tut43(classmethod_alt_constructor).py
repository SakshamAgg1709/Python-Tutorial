# Class Methods As Alternative Constructors

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
        # params =  string.split("-")#It will separate string by "-" and make a list of all th components like - ["Harry" , "30000" , "Student"]
        # return cls(params[0] , params[1] , params[2])


         return cls(*string.split("-"))

karan = Employee.from_str("Karan-30000-Student")
print(karan.salary)
print(karan.name)
print(karan.role)

