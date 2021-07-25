# Pickle Module in Python

import pickle

"""
rb - read binary
wb - write binary
"""

# It is used for preservation or storing a Python object


# Pickling A Python Object
cars = [ "Audi", "Mercedes" ,"Rolls Royce" , "BMW"]
file = "mycar.pkl"
fileobj  =  open(file , 'wb')
pickle.dump(cars, fileobj)# It takes file oject not file - It means is take open file
fileobj.close()

#Unpickling

file = "mycar.pkl"
fileobj = open(file, 'rb' )
mycar = pickle.load(fileobj)
print(mycar)
print(type(mycar))# It is a list

data = [{"ddd" : "ddd",  "ddsds" : "ddd"}]
file2 = "miscellenous.pkl"
file2obj = open(file2 , 'wb')
pickle.dump(data, file2obj)

file3obj = open(file2 , 'rb')
list = pickle.loads(fileobj)
print(list)

