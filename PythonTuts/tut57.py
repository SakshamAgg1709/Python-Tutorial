# Generators in Python

"""
Alo refer iterators.py but it is so confusing
"""
"""
Iterable - object jisme __next__ aur__getitem__ jaise built in methods ho - ye hume iterator deta h 
Iterator - object jisme __next__ method define h
Iteration - kisi ko iterate karna aur uske elements ko fetch karna

"""

"""
Return - ye function ki return value - iske aage function kucch nhi karega
print-  ye python console mein object print karta h 
yeild - ye ek generator h
"""

# for i in range(40):# Isne store nhi kar rakha output ye on the fly generate kar rha h - So range() is a generator
#     print(i)

def gen(n):
    for i in range(n):
        yield i


g = gen(4)
print(g)# Ye value maine generate kar li jab mbhi mujhe need huyi tab main use iterate karunga
print(g.__next__())# Har ek baar naya no. ayega
print(g.__next__())
print(g.__next__())
print(g.__next__())
#print(g.__next__())# LAst wale mein error ayega  kyuki sirf 4 values hi iterate ho sakti h

h = "Harry" # String bhi iterable h

ier = iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())

"""Old video from harry bhai"""

# Generators are iterables

#for i in range(10000000000000000000):
   # print(i)# It will use so much RAM
# """Now we dont want to print the numbers but generate those so that we can use them any time we want"""

def gen(n):
    for i in range(n):
        yield i #It is a keyword - we just yeilding the numbers  not generating them we can generate by using this function


print(gen(10000000))# isne ek object bana jisse aap labhii bhi Generate kar sakte h

"""Us object ko generate karne ke liye ye kare"""

for i in gen(10000):
    print(i)

ob1 =gen(10000000)
print(next(ob1))
print(next(ob1))
print(next(ob1))
print(next(ob1))
print(next(ob1))
#
# num = 345
# for i in num:
#     print(i)# it will throw error - int is not iterable

num = "Saksham"
for i in num:
    print(i)










