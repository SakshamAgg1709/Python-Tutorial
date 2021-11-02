#Dictionary and its Functions

#Dictionary is nothing but key value pairs

d1 = {} #It is a dictionaryS
# print(type(d1))

# d2 = {"Harry" : "Burger" , "Saksham":"Pizza" , "Rohan" : "Fish" ,
#       "Shubham" : {"B" : "fruits" , "L": "roti" , "D" : "Chicken"}}#Yaha shubham ek puri dictionary kha rha h
# d2["ANkit"] = "Junk Food"
# d2[420] = "Kebab"
# print(d2)
# #Now we want to delete ankit
# del d2["ANkit"]#ankit ke sath sath uski key value bhi delete ho jaeygi

# print(d2["Saksham"])
# print(d2["Shubham"] ["B"])#Shubham ki key value mein jo dictionary h uske anndar B ki jo key value h wo print hogi
# print(d2)

# print(d2.copy())

# d3 = d2 #Abb d3 ek nayi dictionary nhi h , WO d2 ko hi as a reference lega
# del d3["Shubham"]# YAha d3 se Shubham delete kia to d2 se bhi delete ho gaya

# print(d2)


# print(d2.get("Harry"))# It is same as => print(d2["Harry"])

# d2.update({"Rina" : "Toffee"})#Rina h hi nhi to Rina dictionary mein add ho jaeygi
# print(d2)

# print(d2.keys())#To print keys
# print(d2.items())#to print items


# d3 = {"Harry" : "Coder"}
# print(d3.get('Harry'))# We use get when Harry is not present in dict - it returns none if we write - .get("Harrry4")
# print(d3['Harry'])# It gives same result but we use it only if the key is present in the dict otherwise it willl return error - if we write - ["Haarry3]

"""Practise"""

emp = {}
while True:
      employee = input("Enter the name of Employee:\n")
      age = int(input("Enter the age of the Employee:\n"))
      salary = int(input("Enter the salary of the Employee:\n"))
      emp[employee] = {}
      emp[employee]['Age'] = age
      emp[employee]['Salary'] = salary
      ask = input("Do you want to add more employees\nType \'y\' for Yes and \'n\' for No:\n")
      if ask =="y":
            continue
      else:
            break
for keys in emp:
      if emp[keys]['Age']>60:
            emp[keys]['Salary'] = 100000

print("Salary of Employees with age more than 60 is replaced with 100000", emp)