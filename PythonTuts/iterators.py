"""Not a from the series of Harry bhai"""
"""But very important"""

num = [ 3,5,2,56]

"""To print numbers one by one"""
print(num[0])
#print(num[8])# it will give an error index out of range

"""or"""
for i in num:
    print(i)

"""or"""
it = iter(num)# WE have converted list into iterator

print(it)#IT will tell you about the object
print(it.__next__()) #it is a in-built function to print value of iterator
print(it.__next__())# It oreserves the old value and print the next value
print(it.__next__())
print(next(it))# It is same as above one
# print(it.__next__())# It will not print more values and throw error because all the prior values are already preserved
# print(it.__next__())
# print(it.__next__())

"""Creating our own iterator"""

class Topten:
    def __init__(self):
        self.num = 1

    def __iter__(self): # It will giv iter of object
        return self

    def __next__(self):

        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration

values = Topten()

# for i in values:
#     print(i)

print(values.__next__())

