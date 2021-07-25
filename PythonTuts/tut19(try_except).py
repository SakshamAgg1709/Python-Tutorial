#Try and Except Exceptional Handling in Python

print("Enter num1")
num1 = input()
print("Enter num2")
num2 = input()

#By using this we can ensure that the next statement will work perfectly
#It will just write the error as a string and continue the programm
try:
    print("Sum =>" ,
      int(num1) + int(num2))
except Exception as e:
    print(e)


print("This line is very important")