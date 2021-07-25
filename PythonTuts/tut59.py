# Using Else with For Loops in Python

khana = ["roti","Sabzi","Chawal"]


"""
For Loop can end in 2 ways:

1 - End of the iterables or the list on which the for loop is running
2 - If there is if condition in for loop and it is not satisfied   
"""
# for item in khana:
#     print(item)
#     break # Yaha else statement work nhi karegi kyuki for loop naturally end nhi hua
# else:
#     print("This for loop ended properly")


for item in khana:
    if item == "roti":
        break# Isme loop break ho gaya to kucch bhi print nhi hoga
else:
     print("Your item was not found")