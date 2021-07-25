# List Comprehensions

ls = []

# for i in range(100):
#     if i%3 == 0:
#         ls.append(i)
#
# print(ls)

"""Shorter method - List comprehension"""

#ls = [i for i in range(100)] # It will print all the nos. form 1 to 100 in the list
ls = [i for i in range(100) if i%3 == 0]# It will print multiples of 3
print(ls)

"""Dictionary Comprehensions"""

# we want to make  dict = {0:"item0" , 1 : "item1"and so on}

# dict = {i:f"item{i}" for i in range(100) if i%100 == 0}
# print(dict)

dict = {i:f"item{i}" for i in range(5)}
dict1 = {value:key for key,value in dict.items()}# WE want to reverse the dict.
print(dict,"\n",dict1)

"""Set Comprehensions"""

dresses = {dress for dress in ["dress1" , "dress2" ,"dress1" , "dress2" ,"dress1" , "dress2"]}# Ye set return karega
"""Set mein value repeat nhi hota isliye sirf dress1 and dress2  hi print hoga"""
print(dresses)

"""Generators Comprehensions - Generators are the functions that can yeild a data and are able to generate it but do not genarate"""

evens = (i for i in range(100) if i%2 == 0)# Here we have used parenthesis - differnt from all above
print(type(evens))
print(evens)
print(evens.__next__())
"""or we can use for loop to iterate all the items"""
for items in evens:
    print(items)

"""Question"""

items = int(input("How many items you want to add in the list :\n"))

t = input("Enter Components of List separated by a space")
t2 = t.split(" ")

print("1 for LIst Comprehensions\n2 for Dictionary Comprehensions\n 3 for Sets Comprehensions ")
choice = int(input("What do u want to make :\n"))

if choice == 1:
    list = {i for i in t2}
    print(list)
    print(type(list))
elif choice == 2:
    dict ={f"Item{i}":i for i in t2}
    print(dict)
    print(type(dict))

elif choice == 3:
    set = {it for it in t2}
    print(set)
    print(type(set))

else:
    print("Enter correct Input")

