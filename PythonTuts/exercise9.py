# Akhbar Padhkar Sunao

import json
import requests

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

"""I was unable to Solve this :(,I saw harry bhai's solution ; But It was not that tough examine it carefully...."""

if __name__  == "__main__":
    url = "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=06ee9275aebd45a995534553b3004c87"
    news = requests.get(url).text
    print(news)
    # print(news["status"])# IT will throw an error
    """News is a string , we cannot do its slicing, so we will convert news into a python object using json module"""
    news_dict = json.loads(news)
    print(news_dict["status"])# Now , it will  work ver fine
    print(news_dict["articles"])
    arts =  news_dict["articles"]
    speak("Today's News")
    for articles in arts:
        speak(articles["title"])
        speak("Moving on to the Next news..Listen Carefully")
    speak("Thanks for Listening....")
