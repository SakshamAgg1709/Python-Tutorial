# Requests Module for HTTP Requests
#
# import requests
# r = requests.get("https://financialmodelingprep.com/api/company/price/AAPL")# It just a API from a website
#
#
# print(r.text)
# print(r.status_code)
#
# url = "www.something.com"
# data = {
#     "p1" : 4,
#     "p2" : 33
# }
#
# r2 = requests.post( url = url , data = data)

"""Computer Class Program"""

# def square(n):
#     i  = 1
#     while i <=5:
#         print(f"{n}^{i} = {n**i}")
#         i += 1
#
# inp = int(input("Enter the number you want to multiply by itself : \n"))
# square(inp)

# inp  = int(input("Enter the no."))
# print("First five multiples are \n")
# i = 1
# for i in range(0,5):
#     print(f" {inp*i}")
#     i += 1

int = int(input("Enter a digit between 0 to 9 :\n"))
print(f"{int}{int+1}{int+2}")