# Function Caching in Python


"""
Caching - Jab humara system internet ke kisi page ya media files ko ek jagah save kar leta h jisse baar-baar wo load hone mein time na le
"""
import time
from functools import lru_cache
"""lru_cache is a decorator"""

@lru_cache(maxsize =2)# Sirf teen values ko cache karega - Jitni maxsize utni hi RAM usage
def some_work(n):
    #Some Task taking n seconds
    time.sleep(n)# Iske place par koi aur command hogi jo bahut time leti h run hone mein
    return n

if __name__ == '__main__':
    print("Now running Some work")
    some_work(3)# We want to run some work for 10 times ,but it will take 30 secs then ,we will store the value of some work anywhere
    some_work(1)
    # some_work(1)
    # some_work(2)# Yaha wo 3 function ko  cache karega so we have to wait 9 sec
    """Function Caching use karke hume baar baar 3 sec. wait nhi karna padega"""
    print("Done... Calling Again")
    some_work(3)# We dont want this delay
    print("Called Again")


inp = int(input("How many values you want to cache"))

@lru_cache(maxsize= inp)
def func1(n):
    time.sleep(n)
    return n


print("Some other work")
func1(45)
func1(3)
func1(66)
func1(4)
func1(2)