#Join function in Python

lis = ["John" , "Cena" ,"Khali" ,"Randy" , "Jinder Mahal" , "Sheamus" , "Orton"]

print("WWE suerstars")

"""Using for loop"""
# for item in lis:
#     # print(item , "and")#Due ti this all names will be in a newline
#     print(item , "and" ,  end = " ")

"""Using join function"""
# a = " and ".join(lis)#joining with and
b  = " , ".join(lis)
# print(a)
print(b)


