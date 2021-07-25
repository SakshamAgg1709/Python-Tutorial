# JSON Module in Python

# JSON - Javascript object Notation  - Way to send Data - Easily Data storage in Browser

import json

data = '{"var1": "Harry" , "var2": 55}'
print(data)# We can write like this but we will parse this data
print(type(data))

parsed = json.loads(data)
print(parsed)
print(parsed['var1']) # We can do this here but cannot do this in - print(data)
print(type(parsed))

# Task 1 = What json.load means and what does it do ?

data2  = {
    "Channel_name": "Saksham Aggarwal",
    "Cars" : "Alto",
   "Skills": ['canva' ,'wordpress', ' python' , 'SEO'],
    "fridge" : ('roti' , 420),
    "isbad" : False
}
"""THey python mein work karega, hum isse ek javacript compatible object mein convert karte h"""

jscomp = json.dumps(data2)
print(jscomp)




