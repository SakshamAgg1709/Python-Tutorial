#Anonymous/Lambda Functions in Python


#It is a normal function
def add(a, b):
    return a + b

#It is one liner function
minus = lambda x , y : x- y

# It is a normal minus function(Both will work similarlry)
# def minus(x,y):
#     RETURN X - Y


print(minus(2,3))

def a_first(a):
    return a[1]


# a = [[12,4] , [5,6] , [0,9]]
# print(a.sort(key = a_first))#  - The sort() method sorts the list ascending by default.#KEY is used to run a function; But sort() function can also be used withou key

a = [[12,4] , [5,6] , [0,9]]
a.sort(key = lambda x:x[1])#Here we have directly used lambda function
print(a)

# s = [[12,4] , [5,6] , [0,9]]
# s.sort()#Here we have directly udsed lambda function
# print(s)

b= [ "Saksham" ,"Harry" ,"Rohan"]
b.sort()
print(b)