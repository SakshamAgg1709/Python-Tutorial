# Open() , Read() and Readlines() for reading file


# f = open("saksham.txt" , "rb")#It is binaary mode

# # f = open("saksham.txt" , "rt") #It is default mode to read and write
# # f = open("saksham.txt" , "r")#it is normal read
# content = f.read()
# content = f.read()
# print(content)
#
# f.close()



f = open("saksham.txt" , "rt")
content = f.read(4) #Only four characters

print(content)



content = f.read(344344)
print("1" , content)


content = f.read(344344)# Yaha content dubara print nhi hoga kyuki wo ek baar access ho chuka h
print("2" , content)

"""Read line by line"""
f2 = open("saksham.txt")
#yaha hum  content = f.read()nhi karenge kyuki isse file pointer 0 ho jaeyga aur for loop mein kucch print nhi hoga
# for line in f2 :
#     print(line, end ="")

"""
Ek baar jo chracter access ho gaya to wo dubara access nhi ho sakta
"""

print(f2.readline())#Read line by line(line1)
print(f2.readline())#(line2)
print(f2.readline())#(line3)

#Shuru ki 3 lines access ho chuki h isliye sirf lasst line access hogi in below function
print(f2.readlines())#It will display whole lines in the form list


f2.close()