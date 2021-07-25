#Enumerate function in Python

l1 = ["Bhindi" , "Aloo" , "Chopsticks" ,"Chowmein"]
#We want to buy only odd items


# i = 1
# for item in l1:
#     if i%2 != 0 :
#         print(f"Jarvis please buy {item}")
#     i += 1

#Here we are starting index from 0
#Enumerate function takes index and item both

"""It is a very good method"""

for index, item in enumerate(l1):
    if index%2 == 0:
        print(f"Jarvis please buy {item}")


