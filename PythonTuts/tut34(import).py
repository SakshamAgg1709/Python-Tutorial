#How import works? in Python


# import sklearn as sk
# print(sk.__version__)

# import sys
# print(sys.path)#Ye wo path show karegaa jahan se wo module laa rha h

# It is a concept of machine learning
# from sklearn.ensemble import RandomForestClassifier
# print(RandomForestClassifier())

#This is normal method to import file1 and get a
# import file1
# print(file1.a)

#Now Advance Method  #But is not advisable

# from file1 import a
# print(a)

#You can put all important functiions in a file use it whenever you want by importing the particular file.
import file1
print(file1.a)
file1.printjoke("Hey! You  are fat")



#Agar aapke computer mein kahi bhi module install h to wo import kar lega but wo aapki directory se hi search karna start karega agar waha koi file uss name se mili to wo error throw karega aur agar nhi mili to aage dundh nikalega

list = [1 ,2 ,3, 3,4,5]
list[1] = 8
print(list)