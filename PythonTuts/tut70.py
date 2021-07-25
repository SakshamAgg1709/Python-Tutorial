# is vs. "==" in python

"""
== - value equality - Two objects have same value
is - reference equality - Two references refer  to the same  object
"""

li = [7, 4,5]
b =li
print(b == li) # It will return True

print(b is li) # It will also return True because they are refering to the same object

b[0] = 0 # THis will also make changes to the list li
print(li)

c = li[:]# Agar ye colon lagaye to c bhi ek list ban jayegi jiski value same hogi but ye dono ek object nhi
"""Agar hum ye colon hata de to  is aur == dono mein true aeyga"""

print(c == li)# True
print(c == b)# True
print(c is li) # False
print(c is b)# False

"""Task"""

a = [22, 88 , "89"]
f = [22, 88 , "89"]

print(a is f)# WO dono same object nhi h
print(a == f)# WO dono alag object but unki value same h

