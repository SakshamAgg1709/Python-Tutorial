# Divide the Apples


# it is a good practise to use try and except
try:
    n = int(input("Enter the number of apple harry have : "))
    mn= int(input("Enter the minimum number : "))
    mx = int(input("What is the maximum number : "))
except ValueError:
    print("Enter integer only! ")
    exit()


while(n> mn and n> mx):
    if mn == mx:
        print("This is not a range.")
        if n % mn == 0:
            print(f"{mn} is the divisor of {n}.")
        else:
            print(f"{mn} is not the divisor of {n}.")
    elif mn < mx:
        for i in range(mn, mx + 1):
            if n % i == 0:
                print(f"{i} is the divisor of {n}.")
            else:
                print(f"{i} is not the divisor of {n}.")
    elif mn > mx:
        print("Please enter the minimum value less than the maximum value.")


