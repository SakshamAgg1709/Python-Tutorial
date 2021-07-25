#Apni Dictionary

d1 = {"Coding" : "Using programming languages to get the computer to behave as desired " ,
      "Web" : "Collection of web pages stored in web servers and connected to local computers through internet" ,
      "App" : "stands for Appication ,It is simply a piece of software that you can get access to and use through internet" ,
      "Internet"  : "Global computer network providing variety of facilities" ,
      "Wi-Fi" : "stands for Wireless Fidelity , a facility allowing computer users to connect to internet wirelessly within a particular area"}

print("Enter the Word from the following ->\nCoding\nWeb\nApp\nInternet\nWi-fi  ")
inp1 = input()
inp2 = inp1.capitalize()
#Or we can write
# inp1 = input("Enter the Word :")

print( inp2 , "=> ", d1[inp2])