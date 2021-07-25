#Break and Continue  Statements in Python

i = 0
#
while(True):#true matlab ye program kabi khatam nhi hoga untill you use break
    if i + 1 < 5:
        i = i + 1# i ki value update karnA imp. h
        continue#Jaise hi i = 4 bana program next statement par chala gaya
        #Jab i ki value 1,2,3 hogi tab wo neeche print statement par jaaeyga hi nhi

    print(i +1 , end =" ")#Abb i = 4 h ,so it will print the value of untill i =44
    if i == 44:
        break #Stop the loop
    i = i + 1 #Break  ke baad ye impliment nhi hoga
#
#
"""Quiz"""
while(True):
    print("\nEnter the number")
    inp = input()
    if int(inp) < 100:
        print("Try again ")
        continue

    if int(inp)>100:
        print("Congo , You have entered a no. greater than 100")
        break

#Upar wala bhi thik h but LENGTHY
#ANOTHER METHOD
while(True):
    inp = int(input("Enter the no."))
    if inp > 100:
        print("Congo")
        break
    else:
         print("Try Agian")
         continue





