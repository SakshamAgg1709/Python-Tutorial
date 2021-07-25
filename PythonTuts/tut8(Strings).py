# String Slicing and Other functions

mystr = "Saksham is a good BOY"#index starts from 0, here S is 0
print(mystr[0:8]) #Here we will get S(0) , a(1) , k(2), s(3); not 4
print(len(mystr))
print(mystr[0:21])
print(mystr[0:77])#77 tak nhi h par wo 21 index tak print kar dega
print(mystr[0:7:2]) # 7 characters tak print karega but beech ka har 1 character chhod kar
print(mystr[0:])
print(mystr[:7])
print(mystr[::]) # It is same as => print(mystr[0:21:1])
print(mystr[::3]) #yaha beech mein 3 characters ka gap h
print(mystr[::3333333])# Yaha beech mein 3333333 characters ka gap h isliye sirf S print hua
print(mystr[-1:0])
"""
 print(mystr[-4:-2])-Yaha picche se count karenge Y(-1),O(-2),B(-3),space(-4): Yaha print hua space(-4),B(-3) bass
Yaha picche se shuru hua aur har 2 character chhod kar
"""
print(mystr[17:19:-1])#It will print only a space
print(mystr[::-1])#Isse bas string ulta hoga nothing more
print(mystr[::-2])# Yaha wo string ulta karega aur har ek character chhod kar print karega
# print(mystr[2:7]) - It will print 2,3,4,5,6 indices

print("\t\t\t\t\t\t\t\t\t\t\t\tString Functions")

#is +  alpha + numerical = isalnum
print(mystr.isalnum()) # it will return false because it is not a alpha numeric string; it has spaces

mystr2 = "Sakshamisagoodboy"
print(mystr2.isalnum())#It will return true as it has no spaces

#is + alpha = isalpha

print(mystr2.isalpha())#It returns true if all character in the string is alphabet
mystr3 = "123Sakshamisagoodboy"
print(mystr3.isalpha())
print(mystr.endswith("boy"))#It ends with "BOY"

print(mystr.count("o"))#it will return 2 because o appears twice in the string
print(mystr.capitalize())#It will capitalize only the first letter
print(mystr.find("is"))#If you start counting from 0 ,at 8th position you will get "is"
print(mystr.lower())
print(mystr.upper())
print(mystr.replace("is","are"))









