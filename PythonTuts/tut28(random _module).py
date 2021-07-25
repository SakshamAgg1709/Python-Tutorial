#Using Python external And Built In Modules

import random

"""
Random is a module and randint(),random() and  choice() are its functions(can only be used in random module
"""

a = [ "Saksham" ," tanishka" ,"Misthi"]


random_number = random.randint(0,5)#It will pick any number between 0 and 5
print(random_number)

rand = random.random()# It generates a random number between 0 and 1

print(rand)

lst  = [ "Star PLus" , "Sab Tv" ,"AAJ TAK" , "CWh"]

choice = random.choice(lst)
print(choice)

