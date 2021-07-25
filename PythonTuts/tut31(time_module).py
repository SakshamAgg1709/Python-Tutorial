#Time module in Python

import time

#Time() ek specific date se ab tak ke seconds batata h
initial = time.time()#Time() is a function of time module.
# Example - ek date se abb tak 10 secends ho chuke h

print(initial)
for i in range(45):
    print("This is For loop ")
"""Abb dobara time() use kare to abb uss specific date se 15 seconds ho chuka hoga jab tak for loop khatam hoga"""
"""intitial mein already 10 seconds save h jo 15 mein se minus hoge aur programme ka running time hoga 5 sec."""
print("For loop ran in " , time.time() - initial , "seconds")
#
#

"""Same procedure h but abb hume dobara time.time() ko new vriable mein store karna hoga """
initial2 =time.time()

k = 0
while(k<=45):
    print("This is while loop ")
    time.sleep(0.5)#It make the program to wait for required seconds
    k+=1#it is same as k = k+1
print("While loop ran in " , time.time() - initial2 , "seconds")


"""
time() function uss specific date sse abbt take ke time ko le aaayega 
localtime() function uss time ko ek localtime mein convert karega jo usse ek tupple mein store karega 
asctime() function uss tuple ek acche format mein display karega 
Ye saare function sirf time module ke h aur usi ke saath use honge
"""
localtime = time.asctime(time.localtime(time.time()))
print(localtime)


