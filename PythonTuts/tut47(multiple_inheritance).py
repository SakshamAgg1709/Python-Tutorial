# Multiple Inheritance in Python

class Employee:
    no_of_leaves  = 8
    var = 9
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






class Player:
    no_of_games = 4
    var = 10
    def __init__(self , name, game):
        self.name = name
        self.game = game

    def printdetails(self):
        return f"The Name is {self.name} and he plays {self.game}"


class CoolProgrammer(Employee , Player):#Employee class mein bhi hume 3 argument dene padhenge || Employee , Player ki order bahut importaant h
   language = "C++"
   var =44
   def lang(self):
       print(self.language)

   pass



harry = Employee("Harry" , 500  , "Instructor")
saksham = Employee("Saksham" , 1000 , "Student")

shubham = Player("Shubham" , ["Cricket"])
# karan = CoolProgrammer()# It will give a error because in Employee class we have 3 arguments in init function
karan = CoolProgrammer("Karan" , 20000 , "Senior Programmer")# Sabse pehle argument mein Employee h aur uska init function sirf 3 argument leta h , agar pehle player argument hota to hum karan mein sirf 2 argument dete kuki player ke init function mein  sirf 2 argument h

det  = karan.printdetails()
print(det)
karan.lang()
print(karan.var)#Agar coolprogrammer ke vaar ko hata de to ye employee ka var print karega aur agar employee ke var ko haata de to ye player ke var ko print karega - This is because of the order of the classes written as argument in CoolProgrammer
