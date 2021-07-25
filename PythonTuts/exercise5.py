# Health Management System
# 3 clients - Harry, Rohan and Hammad

def getdate():
    import datetime
    return datetime.datetime.now()

# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client

def log(c):
    if c == 1:
        a = int(input("Enter 1 for Harry ,2 for Rohan and 3 for Hammed:"))
        if a == 1:
            b = int(input("Enter 1 for food and 2 for exercise:"))
            if b == 1:
                d = input("Type here:\n")
                with open("harryfood.txt" , "a") as f:

                    f.write("\n" + d + "\n Date and Time of logging =>" + str([str(getdate())]))#Yaha plus lagana imp. h kyuki write() function sirf ek argument leta h ;comma lagayenge to more than 1 argument ho jaaeyga

                print("Successfully Written\n Thanks for logging")
            elif b == 2:
                d = input("Type here:\n")
                with open("harryexercise.txt" , "a") as f:
                    f.write("\n" + d + "\n Date and Time of logging =>" + str([str(getdate())]))
                print("Successfully Written\n Thanks for logging")
            else:
                print("Enter correct value")
        elif a == 2:
            b = int(input("Enter 1 for food and 2 for exercise:"))
            if b == 1:
                d = input("Type here:\n")
                with open("rohanfood.txt" , "a") as f:
                    f.write("\n" + d + "\n Date and Time of logging =>" + str([str(getdate())]))
                print("Successfully Written\nThanks for logging")
            elif b == 2:
                d = input("Type here:\n")
                with open("rohanexercise.txt" , "a") as f:
                    f.write("\n" + d + "\n Date and Time of logging =>" + str([str(getdate())]))
                print("Successfully Written\nThanks for logging")
            else:
                print("Enter correct value")
        elif a == 3:
            b = int(input("Enter 1 for food and 2 for exercise:"))
            if b == 1:
                d = input("Type here:\n")
                with open("hammadfood.txt" , "a") as f:
                    f.write("\n" + d + "\n Date and Time of logging =>" + str([str(getdate())]))
                print("Successfully Written\nThanks for logging")
            elif b == 2:
                d = input("Type here:\n")
                with open("hammadexercise.txt" , "a") as f:
                    f.write("\n" + d + "\n Date and Time of logging =>" + str([str(getdate())]))
                print("Successfully Written\nThanks for logging")
            else:
                print("Enter correct value")
        else:
            print("Enter correct value")
    else:
        print("Enter correct value")


def retrieve(c):
    if c == 2:
        a = int(input("Enter 1 for Harry ,2 for Rohan and 3 for Hammed:"))
        if a == 1:
            b = int(input("Enter 1 for food and 2 for exercise:"))
            if b == 1:

                with open("harryfood.txt") as f:
                    op = f.read()
                    print("\n" , op , "\nDate and Time of Retrieving =>" , str(getdate()))

                print("Successfully Retrived\nThanks for retrieving")
            elif b == 2:

                with open("harryexercise.txt") as f:
                    op = f.read()
                    print("\n" , op , "\nDate and Time of Retrieving =>" , str(getdate()))
                print("Successfully Retrived\nThanks for retrieving")
            else:
                print("Enter correct value")
        elif a == 2:
            b = int(input("Enter 1 for food and 2 for exercise:"))
            if b == 1:

                with open("rohanfood.txt") as f:
                    op = f.read()
                    print("\n" , op , "\nDate and Time of Retrieving =>" , str(getdate()))
                print("Successfully Retrived\nThanks for retrieving")
            elif b == 2:

                with open("rohanexercise.txt") as f:
                    op = f.read()
                    print("\n" , op , "\nDate and Time of Retrieving =>" , str(getdate()))
                print("Successfully Retrived\n Thanks for retrieving")
            else:
                print("Enter correct value")
        elif a == 3:
            b = int(input("Enter 1 for food and 2 for exercise:"))
            if b == 1:

                with open("hammadfood.txt") as f:
                    op = f.read()
                    print("\n" , op , "\nDate and Time of Retrieving =>" , str(getdate()))
                print("Successfully Retrived\n Thanks for retrieving")
            elif b == 2:

                with open("hammadexercise.txt") as f:
                    op = f.read()
                    print("\n" , op , "\nDate and Time of Retrieving =>" , str(getdate()))

                print("Successfully Retrived\n Thanks for retrieving")
            else:
                print("Enter correct value")
        else:
            print("Enter correct value")
    else:
        print("Enter correct value")



print("Health Management System")
inp = int(input("What do you want do?\nPress 1 for logging the data and 2 for retrieving the data:  "))

if inp == 1:
    log(inp)
elif inp == 2:
    retrieve(inp)
else:
    print("Enter Correct Values")