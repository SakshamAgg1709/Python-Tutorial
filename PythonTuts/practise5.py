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

