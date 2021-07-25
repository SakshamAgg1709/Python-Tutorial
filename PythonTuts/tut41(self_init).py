# Self & __init__() (Constructors) in Python

class Employee:
    no_of_leaves  = 8

    # Self is that instance on which the function is workng EX - harry.printdetails() - here self is harry
    def __init__(self , aname ,asalary , arole):#Iss __init__ function ko dubara likhne ki need nhi h
        self.name = aname
        self.salary  = asalary
        self.role  = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"



harry = Employee("Harry" , 5000000000  , "Instructor")#Yaha __init__ function automatically work kar rha h because it is a constructor
saksham = Employee("Saksham" , 100000000000000000 , "Student")

# harry.name = "Harry"
# harry.salary = 500000000000
# harry.role  = "Instructor"
#
# saksham.name = "Saksham"
# saksham.salary = 10000000000000
# saksham.role  = "Student"

print(saksham.printdetails())#print detail function ka argument saksham h , isse handle karne ke liye functon mein self lagaya h
# Ye argument wala concept sirf Object oriented Programming mein use hota h
#Agar self na ho to error dega

print(harry.printdetails())

print(saksham.name)

