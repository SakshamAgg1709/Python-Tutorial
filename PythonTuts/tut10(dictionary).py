#Dictionary and its Functions

#Dictionary is nothing but key value pairs

d1 = {} #It is a dictionaryS
# print(type(d1))

d2 = {"Harry" : "Burger" , "Saksham":"Pizza" , "Rohan" : "Fish" ,
      "Shubham" : {"B" : "fruits" , "L": "roti" , "D" : "Chicken"}}#Yaha shubham ek puri dictionary kha rha h
d2["ANkit"] = "Junk Food"
d2[420] = "Kebab"
print(d2)
#Now we want to delete ankit
del d2["ANkit"]#ankit ke sath sath uski key value bhi delete ho jaeygi

print(d2["Saksham"])
print(d2["Shubham"] ["B"])#Shubham ki key value mein jo dictionary h uske anndar B ki jo key value h wo print hogi
print(d2)

print(d2.copy())

d3 = d2 #Abb d3 ek nayi dictionary nhi h , WO d2 ko hi as a reference lega
del d3["Shubham"]# YAha d3 se Shubham delete kia to d2 se bhi delete ho gaya

print(d2)


print(d2.get("Harry"))# It is same as => print(d2["Harry"])

d2.update({"Rina" : "Toffee"})#Rina h hi nhi to Rina dictionary mein add ho jaeygi
print(d2)

print(d2.keys())#To print keys
print(d2.items())#to print items