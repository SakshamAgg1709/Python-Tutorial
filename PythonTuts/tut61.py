# Else and Finally eith try & Except in Python

f1 = open("saksham.txt")

try:
    f = open("does2.txt")

except EOFError as e:
    print("EOFError aa rha h")
    print(e)

except IOError as w:
    print("IOE Error aa rha h ")
    print(w)


else:# ye tabhi run karega jab except run nhi ho rha
    print("This will run only if except is not running")

finally:# Finaly aisa to karna hi karna h chahe code try ke andar ghuse ya phir except ke andar
    print("Run this anyway....")
    # f.close() # f variable ke koi file hi nhi h
    f1.close()

print("Important Stuff")
