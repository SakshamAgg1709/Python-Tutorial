# Making a reccursive function to calculate the sum of first n natural numbers

# Logic is - sum(n) = sum(n-1) + n

# def sum_first_n(n):
#     if n == 1:
#         return 1
#     else:
#         return n + sum_first_n(n-1)
#
# int = int(input("Enter the number"))
#
#
# print(sum_first_n(int))


"""Q. 3"""
# num1 = int(input("Enter first number"))
# num2 = int(input("Enter second number"))
# num3 = int(input("Enter third number"))
# num4 = int(input("Enter fourth number"))
#
# li = [num1 ,num2, num3, num4]
# li.sort()
# print(f"The highest number is {li[3]}")
# print(f"The second highest number is {li[2]}")

# str = input("Enter any number")
# str = str[::-1]
# print(str

inp = input("Enter any string:\n")
# inp2 = inp.lower()
# inp3 = inp.upper()
#
#
#
# print(f"Lower Case of entered string - {inp2}\nUppercase of Entered String - {inp3}")

"""Long Method for the above function"""

for i in inp :
    if ord(i)>=97 and ord(i)<=122:
        print(chr(ord(i) - 32), end = "")
    else:
        print(chr(ord(i)- 97), end = " ")

print(inp)

high = 0

while(True):
    inp = int(input("enter the number"))
    li = []
    li.append(inp)
    if inp == 0:
        break
        li2 = li.sort()
        li3 = li2.reverse()
        high = li3[0]
    else:
        continue


""""Or we can use the below code"""
# num = -1
# h = 0
# while(num!=0):
#     num = int(input("Enter the number"))
#     if h<= num:
#         h = num
#
print(f"The highest number entered by you is {high}")





str1 = input("Enter any positive number")
dig = [int(x) for x in str(str1)]
sum = sum(dig)
print(sum)

"""Changing String sentence with first letter of each word capital """

str1 = input()
str2 = ""

l = len(str)
i = 0

while i<l:
    if  i==0:
        str2  = str2  + str1[0].upper()
        i = i + 1
    elif str1[i] == '' and str1[i+1] != " ":
        str2 = str2 + str1[i]
        str2 = str2 + str1[i + 1].upper()
        i = i + 2
    else:
        str2 = str2 + str1[i]
        i = i + 1


print(str2)

"""Printing Pyramid Pattern"""
# Function to demonstrate printing pattern triangle
def triangle(n):
    # number of spaces
    k = n - 1

    # outer loop to handle number of rows
    for i in range(0, n):

        # inner loop to handle number spaces
        # values changing acc. to requirement
        for j in range(0, k):
            print(end=" ")

        # decrementing k after each loop
        k = k - 1

        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i + 1):
            # printing stars
            print("* ", end="")

        # ending line after each row
        print("\r")


# Driver Code
n = 5
triangle(n)

"""TO Add Matrices"""

# WAP add to matrices.
r = int(input("Enter how many rows"))
c = int(input("Enter how many col"))

# to load matrix 1
main1 = []
for i in range(0, r):
    l = []
    for j in range(0, c):
        n = int(input("Enter value"))
        l.append(n)
    main1.append(l)

# to load matrix 2
print("enter values for matrix2")
main2 = []
for i in range(0, r):
    l = []
    for j in range(0, c):
        n = int(input("Enter value"))
        l.append(n)
    main2.append(l)

print("Matrix 1")
for i in range(0, r):
    for j in range(0, c):
        print(main1[i][j], end=" ")
    print()

print("Matrix2")
for i in range(0, r):
    for j in range(0, c):
        print(main2[i][j], end=" ")
    print()
# adding both the matrics
main3 = []
for i in range(0, r):
    l = []
    for j in range(0, c):
        l.append(main1[i][j] - main2[i][j])
    main3.append(l)

print("Matrix3")
for i in range(0, r):
    for j in range(0, c):
        print(main3[i][j], end=" ")
    print()