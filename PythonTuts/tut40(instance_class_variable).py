# INstances & Class Variables in Python

class Employee:
    no_of_leaves  = 8
    pass


"""Hum Humesha sabse pehle Object ke personal variable ko dekhenge jise instance variable kehte h - phir hum class variable par jaenge"""
print(Employee.__dict__)
harry = Employee()
saksham = Employee()

harry.name = "Harry"
harry.salary = 500000000000
harry.role  = "Instructor"

saksham.name = "Saksham"
saksham.salary = 10000000000000
saksham.role  = "Student"

print(harry.no_of_leaves)
print(saksham.no_of_leaves)
print(Employee.no_of_leaves)
Employee.no_of_leaves  = 9

print(saksham.__dict__)#Isme  no of leaves nhi aaaeyga kyuki vo variable sirf Employee mein h

print(Employee.no_of_leaves)
saksham.no_of_leaves = 10 # It creates a instance variable ; personal property of an object;only saksham object has changed
print(saksham.no_of_leaves)
print(harry.no_of_leaves)

print(saksham.__dict__)#Yaha saksham object meinn bhi no of leaves add ho chuki h

print(Employee.__dict__)# Yaha no of leaves 9 hi h


