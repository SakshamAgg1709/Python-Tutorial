# OS Module in Python - :o - Very Important

import os # (Built-IN MOdule)

# print(type(os))
# print(dir(os))

# print(os.getcwd())#cwd- current working directory
# os.chdir("C://")# Changing Directory
# print(os.getcwd())# Abb baki saare tuts ko hum import nhi kar sakte
# f = open("harryfood.txt")# It will get error because we are now in a different directory

print(os.listdir())# Ye saari files and folder ko display karega jo bhi directory mein h -ek list ki form me
print(os.listdir("D://"))# Meri d - Drive mein jo bhi files and folders h wo show karega
# os.mkdir("This")#Maing a new folder in current Directory
# os.makedirs("This/That")# Maine multiple new folders or directory  in current Directory
# os.rename("harryfood.txt" , "harryfoooood.txt")
print(os.environ.get('Path'))# Getting a environment variable
print(os.path.join("C://" , "/saksham.txt"))# Ye Path ko join karta h - Agar beech mein jyaada ya kam backslashes h to ye usse correct kar deta h

print(os.path.exists("C://"))# Agar C:// name ki koi directory h to True return karega agar nhi h to False return karega
print(os.path.isdir("C:/"))# C: namme ki directory h to True return karega
print(os.path.isfiles("C:/"))# C:/ name ki koi file nhi isliye False return karega

"""There are many more functions - Check them in the documentation of Python"""