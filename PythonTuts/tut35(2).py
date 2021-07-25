#if__name__ == __main__ in Python

"""
Now we  ant to use the functions of tut35 in this file but don't want the other code
"""
import tut35

print(tut35.add(5, 3))#Ye saara code tut35 ka execute kar dega jab tak hum main nhi banate

#now if we want to use a specific function of any file we create __main__
print(__name__)# Yaha bhi main hi print hoga
