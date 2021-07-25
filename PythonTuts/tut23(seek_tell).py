#Seek() , Tell() and more in Files in Python

f = open("saksham.txt")
"""
readline() - isse har ek line alag alag line mein print hogi 
readlines()  - isse har ek line ek hi line mein list ke tarah print hogi 
"""
print(f.tell())#It tells you the positon of your file pointer
print(f.readline())
print(f.tell())
print(f.seek(0))#Isse file pointer dubara 0 par aa gaya aur first line print kardi
print(f.readline())
print(f.tell())
print(f.seek(10))#Abb file pointer 10th character par aa gaya
print(f.readline())


f.close()