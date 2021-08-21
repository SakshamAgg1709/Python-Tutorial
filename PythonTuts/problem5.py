print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tPalindromify the list")

"""
Problem Statement:-
You are given a list that contains some numbers. You have to print a list of next palindromes only if the number is greater than 10; otherwise, you will print that number.

Input:
[1, 6, 87, 43]

Output:
[1, 6, 88, 44]
"""
'''
Author : Saksham Aggarwal
Date : 21/08/21
Purpose : Solving Problem 5 from Code With Harry Python Playlist
'''
def next_palindrome(n):
    n = n+1
    while not is_palindrome(n):
        n += 1
    return n


def is_palindrome(n):
    return str(n) == str(n)[::-1]


if __name__ == "__main__":
    n = int(input("Enter the number elements in list\n"))
    li = []
    for i in range(n):
        number = int(input("Enter the number:\n"))
        li.append(number)
    print(f"You have entered {li}")
    # li2 = []
    # for i in li:
    #     if i > 10:
    #         i2 = next_palindrome(i)
    #         li2.append(i2)
    #     else:
    #         li2.append(i)
    print(f"Output List : {[li[i] if li[i] < 10 else next_palindrome(li[i]) for i in range(n)]}")
