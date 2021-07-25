# Object Inrtospection in Python

class Employee:
    def __init__(self ,fname,lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithharry.com"

    def explain(self):
            return f"This employee is{self.fname} {self.lname}"
    @property
    def email(self):
        if self.fname == None or self.lname == None :
            return "Email is not set"
        return f"{self.fname}.{self.lname}@codewithharry.com"
        pass

    @email.setter
    def email(self ,string):
        print("Setting now....")
        names = string.split("@")[0]#It will return a list
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        """We use none to delete in OOP"""
        self.fname =None
        self.lname =None


skillf = Employee("Skill" , "f")
#print(skillf.email)

print(type(skillf))
print(type("This is  a string"))# Ye string ek object h jo str class se aayi h
print(id("This is  a string"))
print(id("This is  a string"))# THe ID of both the string is same because they have same letters
print(id("Every object has different ID"))

o = "THis is a string"
print(dir(o))# It rpints all the methods or function we can use in a string

import inspect # There are many features of insoect element

print(inspect.getmembers(skillf)) # All the memebers of skillf

"""Challenge Accepted"""

