# For Loops in Python

list1 =["Saksham" ,"Harry", "Carry" ,"Rohan"]# WE CAN ALSO USE THIS FOR TUPPLE
for item in list1:
    print(item)

list2 =[["Saksham", 1] ,["Harry", 2] , [ "Carry" , 45] , ["Rohan" , 23]]
for item in list2:
    print(item)

for item,lollypop in list2:#HERE WE CAN TYPE ANYTHING IN PLACE OF  LOLLYPOP
    print(item ,"and lolly is" , lollypop)

#We have typecaste the list into dictionary
dict1 = dict(list2)#HERE WE CANNOT TYPCASTE LIST1 BECAUSE IT HAS ONLY KEYWORD NOT VALUES;LIST2 HAS BOTH
# print(dict1)


#IT IS SAME BUT HERE WE HAVE USED DICTIONARY
# for item,lollypop in dict1.items():
#     print(item ,"and lolly is" , lollypop)

for item in dict1:#jab tak hum comma lagaa kar koi aur variable assign nhi karenge tab tak key values print nhi hogi
    print(item)

"""Quiz"""

#print all the integers which is greater than 6 from the list

list3 = [23 , "Saksham" ,78 ,"rohan" , 3 ,4 , "rahul " ,67 ]

#Pehle sab item ko string banaya phir check kia ki vo numeric h ya nhi aur phir check kia ki vo 6 se greater h ya nhi
for item in list3:
    if str(item).isnumeric() and item>6:
        print(item)



