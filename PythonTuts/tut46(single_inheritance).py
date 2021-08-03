# Single Inheritance in Python

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

class Programmer(Employee):
    """
    Yaha already name,salary,role jaise  variable aa chuke h kyuki uski puri class hi aaa chuki h
    """
    no_of_holidays = 200

    def __init__(self , aname ,asalary , arole , languages):
        """Again we will not copy paste but we will use super keyword but we will learn super keyword later """
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.language = languages


    def printprog(self):
        return f"The Programmer's  name is {self.name} ,Salary is {self.salary} and role is {self.role}.Languages learnt are {self.language}"
    pass
    """    
    We want all the functions of Employee class here
    BUT copy pasting ek bahut hi ghatiyaa method h - isse code reusability ka concept danger mein chalaa jaeyga
    so, Here we will use single inheritance  - Programmer(Employeee)
    """



harry = Employee("Harry" , 500  , "Instructor")
saksham = Employee("Saksham" , 1000 , "Student")

rohan  = Programmer("Rohan" , 3000 , "Junior Programmer"  , ["Python"])
karan  = Programmer("Karan" , 6000 , "Senior Programmer" , ["C++" , "Java" , "Javascript"])

print(karan.printprog())#Humne function  mein return use kiya h to yaha print use karenge
print(rohan.printprog())
print(karan.printdetails())
print(karan.no_of_holidays)
