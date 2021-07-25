#Writing and Appending the filein Python

# f = open("saksham2.txt" , "w")
# #If you are taking a no existing file,it will create one and write the content
# #If you are working on a existing file , it will replace all the matter and write the content
# f.write("This is fourth line")#It will clean the whole file write this.
#



# f = open("saksham2.txt" , "a")#You can "add" the content
# # Jitni baar run karoge utni baar print hogaye
# f.write("This is fourth line\n")
# a = f.write("This is fourth line\n")
#
# print(a)#It will show how much characters you have added. It will display same no. both in write and append mode.




"""Handle read and write mode"""

f = open("saksham2.txt" , "r+")# r+  =  read and write
print(f.read())
f.write("Thank You\n")

f.close()


