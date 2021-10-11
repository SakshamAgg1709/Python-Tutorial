print("Fake Multiplication Tables - Rohan Das is a Fraud")
"""
Problem Statement:-
 Rohan das is a fraud by nature. Rohan Das wrote a python function to print a multiplication table of a given number and put one of the values (randomly generated) as wrong.

Rohan Das did this to fool his classmates and make them commit a mistake in a test. You cannot tolerate this!

So you decided to use your python skills to counter Rohan’s actions by writing a python program that validates Rohan’s multiplication table.

Your function should be able to find out the wrong values in Rohan’s table and expose Rohan Das as a fraud.

Note: Rohan’s function returns a list of numbers like this

Rohan Das’s Function Input:
rohanMultiplication(6)

Rohan’s function returns this output:
[6, 12, 18, 26, …., 60]

You have to write a function isCorrect(table, number) and return the index where rohan’s function is wrong and print it to the screen! If the table is correct, your function returns None
"""

'''
Author- SakshamAggarwal
Date - 11.10.21
Purpose - Solving Problem 8 from Harry Bhai's playlist
'''

import random

def rohanMultiplication(n):
    """
    It is a function made by Rohan to spoil the multiplication table 
    """
    wrongIndex = random.randint(3,9)
    table = [i*n for i in range(1,11)]
    table[wrongIndex] = table[wrongIndex] + random.randint(1,5)
    return table

# print(rohanMultiplication(6) )   

def isCorrect(table, number ):
    for i in range(1,11):
        if table[i-1] != i*number:# - 1 is for matcing the index with  i*number
            return i-1
    return None 

if __name__ == "__main__":
    number = int(input("Entert any number:\n"))       
    rohanTable = rohanMultiplication(number)
    print(rohanTable)
    print(f"The above table is wrong at index {isCorrect(rohanTable,number) + 1}\nThe correct answer is {number*(isCorrect(rohanTable,number)+1)} ")