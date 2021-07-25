# Setters and Property Decorators in Python

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


hindustani_supporter = Employee("Hindustani" ,"Supporter")
nikhil = Employee("Nikhil" ,"Raj")
# print(hindustani_supporter.email)

hindustani_supporter.fname = "US"
#print(hindustani_supporter.email)# It will not change fname in email beacause at the time of object creation ,we have set Hindustani as the fname and constructor has set the email with the previous fname
"""To solve this problem we have Setters"""
#print(hindustani_supporter.email())# But here it not good to use function
print(hindustani_supporter.email)#This works due to adding @property decorator above email method
#hindustani_supporter.email  = "this.that@codewithharry.com"# NOw this will d=show error beacuse we cant change email attribute  without ussing setter
hindustani_supporter.email = "this.that@codewitharry.com"
print(hindustani_supporter.email)
print(hindustani_supporter.fname)

"""NOw we want to delete email"""

del hindustani_supporter.email # It will throw error untill we add deletor
print(hindustani_supporter.email)#It will print None.None@cwh.com untill we add a f statement in email method under the decorator @property