# Class methods in python

class Employee:
    no_of_leaves  = 8
    def __init__(self , aname ,asalary , arole):
        self.name = aname
        self.salary  = asalary
        self.role  = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod # isse main class ya instance kisika bhi variabe change kar sakta hu
    def change_leaves(cls , newleaves):#ye self ke variaable ko nhi nhi balki pure class ka variable change kar sakta h; cls = class
        cls.no_of_leaves = newleaves




harry = Employee("Harry" , 5000000000  , "Instructor")
saksham = Employee("Saksham" , 100000000000000000 , "Student")

Employee.change_leaves(20)

print(Employee.no_of_leaves)
print(saksham.no_of_leaves)
print(harry.no_of_leaves)

saksham.change_leaves(30)# saksham ke saaath ffunction uss kiya but puri class ke no_of_leaves change ho gaye

print(Employee.no_of_leaves)
print(saksham.no_of_leaves)
print(harry.no_of_leaves)

harry.change_leaves(40)

print(Employee.no_of_leaves)
print(saksham.no_of_leaves)
print(harry.no_of_leaves)

