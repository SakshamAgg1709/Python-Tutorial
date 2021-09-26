print("Search Engine")

"""
Problem Statement:-
You are given few sentences as a list (Python list of sentences). Take a query string as an input from the user. You have to pull out the sentences matching this query inputted by the user in decreasing order of relevance after converting every word in the query and the sentence to lowercase. Most relevant sentence is the one with the maximum number of matching words with the query.

Sentences = [“Python is cool”, “python is good”, “python is not python snake”]


 
Input:
Please input your query string

“Python is”

Output:
3 results found:

python is not python snake
python is good
Python is cool
"""

"""
Author - Saksham Aggarwal
Date - 26.09.21
Purpose - Problem 7 from the playlist of CwH
"""
import time



relevance = 0



def matchingWords(sentence1, sentence2):
    words1 = sentence1.strip().split(" ")
    words2 = sentence2.strip().split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            # print(f"Matching {word1} with {word2}")
            if word1.lower() == word2.lower():
                score += 1
    return score

if __name__ == "__main__":
    # print(matchingWords("this is good boy girl", "python is good boy"))
    s1 = "Computer is a very powerful tool"
    s2 = "It has 2 parts - Hardware and Software"
    s3 = "Python is a programming language used for Web Development, Machine Learning, Artificial Intelligence and much more"
    s4 = "Programming is very interesting subject to learn"
    s5 = "Python is a very easy language to learn."
    sentences = [s1, s2, s3, s4, s5]

    query = input("Please input your query string:\n")

    instant = time.time()

    scores = [matchingWords(query, sentence) for sentence in sentences]
    # print(scores)
    sortedSentScore = [sentScore for sentScore in sorted(zip(scores, sentences), reverse=True) if sentScore[0] != 0]
    #Agar user ne sirf space hi enter kar diya t score 0 hoga to phir sentScore jo list h uska 0 element bhi 0 hoga
    # print(sortedSentScore)
    print(f"{len(sortedSentScore) } results found in {time.time() - instant} s")
    for score, item in sortedSentScore:
        print(f"\"{item}\" : with a score of {score}")
