# Sets in Python

s = set()
# print(type(s))

s_from_list = set([1, 2, 3, 4])#This is a set -syntax of set => ([])

# print(s_from_list)
# print(type(s_from_list))

#Or we can write that
# l = [1,2,3,4]
# s_from_list = set(l)#Here it will change a list into set
# print(s_from_list)

#Set is special because it retains only unique values , unlike lists.
#Here it will not repeat 1 again and again
s.add(1)
s.add(1)#Here it will not add 1 because in one set there can only be unique characters
s.add(2)
print(s)

s1 = s.union({1,2,3})
print(s1)#1,2 mein 1,2,3 unite hoye to bana 1,2,3 ; ! aur 2 repeat nhi hoga
print(s,s1)

# print(len(s1))#Similarly we can use min and max
s1 = s.intersection({1,2,3})#1 and 2 are same in both the sets
print(s1)#S aur s1 mei jo values common thi vo print hui
s1 = {4 , 6}
s.isdisjoint(s1)

print(s.isdisjoint(s1))# It means that s1 has completely different values as that of s; IN this case s has 1,2,3 aand s1 has 4,6 so the answer is yes means True

s.remove(2)
print(s)