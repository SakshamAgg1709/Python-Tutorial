#Lists In Python and its functions

grocery = ["Samosa" , "vim bar" , "Sabzi" , "fruits" , "deodrant" , 56]
"""Here also index starts from 0"""
# print(grocery[0])
# print(grocery[1])
# print(grocery[2])
# print(grocery[3])
# print(grocery[4])
numbers = [2,10,3,56,7]
# # print(numbers)
# # print(numbers[2])
# # numbers.sort() #It will arrange the list in asending order
# #
# # numbers.reverse()
# # print(numbers)
#
"""
They will print all numbers
print(numbers[:5])
print(numbers[:])
"""
print(numbers[1:])
print(numbers[1:4])
print(numbers[::2])#Har doosra number print karega ye
print(numbers[::3])#Har teesra number print karega ye
print(numbers[::-1])
print(numbers[::-3])#REverse karke har teesra number print karega #Negative slicing mein -1 se kam mat lena
print(numbers[1:5:-3])
print(numbers[1:5:2])
#
print(min(numbers))#It will return minimum value
print(max(numbers))
numbers.append(7)#It means that you can add one more value in the last
numbers.append(333)
numbers.append(12)
print(numbers)
#
num2  = []
num2.append(1)
num2.append(2)
num2.append(3)
print(num2)
#
numbers.insert(1,67) # 1 is the index and 67 is the no. to be added at that index
print(numbers)#! index par jo 10 tha wo wahi rahega replace nhi kia h ,10 abb index 2 par jaeyga
#
# numbers.remove(67)
# print(numbers)
#
# numbers.pop()# It will remove the last value or the number
# print(numbers)
#
# numbers[1] = 34 #It will replace no. on index 1 with 34
# print(numbers)

# Mutable = can change
# Immutable = cannot change

tp = (1,2,3) #It  has paranthesis,not square bracket, so it is a tuple
#tp[1] = 4 # we cannot change any value of tuple


#tp = (1)# Only one element is not called a tuple untill and unlesss we do not add a comma
tp = (1,)#Now it is a tupple
print(tp)

a = 1
b = 2


# It is a old and traditional method to swap any two numbers
# temp = a
# a = b
# b = temp

#NEW PYTHON METHOD TO SWAP ANY TWO NUMBERS
a,b = b, a
print(a,b)

#My own Project1

print("Enter the MRP")
inp1 = input()

print(" How much Discount is applied?(avoid percent sign)")
inp2 = input()

dis = int(inp2)/100 * int(inp1)
print("Discount price =>" , dis )
print("Price to be PAID =>" , int(inp1) - dis )

