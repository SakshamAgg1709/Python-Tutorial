#Coroutines in Python

# Hum function ko aadha chalaye ek baar aur jabdusri baar chalay to wo vhi se run ho

def searcher():
    import time
    """Some 4 seconds time consuming task"""
    book = "This is a book ON harry and code with harry"
    time.sleep(4)

    while True:
        text = (yield)# Isse python ko pata chal gaya ki searcher function ek coroutines h
        if text in book:
            print("Your text is in the book")
        else:
            print("Your text is not in the book")


"""This is a coroutine not a function"""

search = searcher()
print("Search Started")
next(search) # Isme 4 second wala code run hua
print("Next method Run ")
search.send("harry")#
# input("Press any key")
# search.send("and")# Dubara isme 4 second ka delay nhi lega
# input("Press any key")
# search.send("Saksham")
# input("Press any key")
# search.send("Is")
# input("Press any key")
# search.send("njxn")

"""we can close this coroutine"""

search.close()

# search.send("harry")# It willthrow a stopIteration error

"""Challenge Accepted"""

def searcher2():
    import time
    names = ["Saksham", "Harry" , "Abhishek" ,"Vishwesh", "Vishesh" ,"CarryMinati", "Yash Khandelwal"]
    time.sleep(3)

    while True:
        yoyo = (yield )
        if yoyo in names:
            print("Your name is in the list")
        else:
            print("Your name is not in the list")


search2 = searcher2()

print("List of name is being generated")
next(search2)
print("List of name has been generated")
nam = input("Enter your name\n")
nam2 =nam.capitalize()
search2.send(nam2)

