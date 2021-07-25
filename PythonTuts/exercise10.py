# Pickling Iris DataSet

import pickle
import requests

data  = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text
# print(data)
#
# l1 = data.split("\n")
# # print(l1)
"""List Comprehensions are better way to make lists"""
l2 = [ item.split(",") for item in data.split("\n") if len(item) != 0]
print(l2)

with open("myiris.pkl", "wb") as f:
    pickle.dump(l2, f)
    """Hume l2 dump karna h to wo pehle aaeyga aur f mein dumpkarna h to wo baad mein aaeyga"""
# Pehle humesha dump hota h phir load hota h

"""To read the pkl file"""

with open("myiris.pkl", "rb") as f:
    print(pickle.load(f))