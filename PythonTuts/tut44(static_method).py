# Static Methods in Python

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


    @staticmethod
    def printgood(string):#It can be run only in this class object

        print("This is good" + string)#It doesn't take self or cls as an argument
        # It can be used by class as well as any instance - Ye koi argument nhi leta - It is just a common function used to rpint a string but it is written in this class so that only the objects of this class only




karan = Employee.from_str("Karan-30000-Student")
saksham = Employee.from_str("Saksham-300000-student")
print(karan.salary)
print(karan.name)
print(karan.role)

karan.printgood(" Saksham")
Employee.printgood("work")
saksham.printgood("work")
