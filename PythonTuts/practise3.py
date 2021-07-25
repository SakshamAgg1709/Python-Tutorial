a = int(input("Enter the value of A:\n"))
b = int(input("Enter the value of B:\n"))
c = int(input("Enter the value of C:\n"))

if a>b and a>c:
    print("A is the largest")
elif b>a and b>c:
    print("B is largest")
elif c>a and c>b:
    print("C is the largest")
else:
    print("Enter correct input")
