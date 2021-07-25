# if__name__ == __main__ in Python


def printhar(string):
    return f"Ye string harry ko de de thakur - {string}"


def add(num1, num2):
    return num1 + num2 + 5

#Ye humne main code se bahar rakha hto ye dusri file mein run hoga
print("and the name is ", __name__)#Yaha __name__ ki value __main__ h but jiss file mein ye import hoga waha  __name__ ki value tut35 hogi jisse pata chalega ki ye code tut35 se import hua h

# Ye main content h jo sirf iss file mein execute hoga
#Agar hum ye file export karte h to main walaa code dusri file mein nhi run hoga
if __name__ == '__main__':

    print(printhar("Saksham"))
    o = add(2, 4)
    print(o)
