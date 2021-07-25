# Regular Expressions in Python

import re

mystr = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
+919899334343
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass,
'''

"""
Functions in Regex

findall: It finds all search for matches and print resultant in the form of a list.
search: It works the same as a findall, but the resultant is a matched object, if any found.
split: The split function splits the string from every matched into two new strings.
sub: The sub-function works exactly like a replace function in notepad or MS Word, it replaces the original word, with a word of our choice.
finditer: The finditer yields an iterator as a resultant with all the objects that match the one we sent it) finditer supports more attributes than any other function defined above. It also provides more details related to the matched object. So, most of the examples we are going to see next will contain a finditer function in them.

'.': Matches any single character except newline
'$': Anchors a match at the end of a string
' *': Matches zero or more repetitions
'+':Matches one or more repetitions
'{}':Matches an explicitly specified number of repetitions
'[]':Specifies a character class

[] A set of characters
\ Signals a special sequence (can also be used to escape special characters)
. Any character (except newline character)
^ Starts with
$ Ends with
* Zero or more occurrences
+ One or more occurrences
{} Exactly the specified number of occurrences
| Either or
() Capture and group
Special Sequences
\A Returns a match if the specified characters are at the beginning of the string
\b Returns a match where the specified characters are at the beginning or at the end of a word r"ain\b"
\B Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word

\d Returns a match where the string contains digits (numbers from 0-9)
\D Returns a match where the string DOES NOT contain digits
\s Returns a match where the string contains a white space character
\S Returns a match where the string DOES NOT contain a white space character
\w Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
\W Returns a match where the string DOES NOT contain any word characters
\Z Returns a match if the specified characters are at the end of the string
"""

# patt = re.compile(r'fass')
#
#
# print("\n")
# print(r"\n")# You will understand the r''
#
# matches = patt.finditer(mystr)
# for match in matches:
#     print(match)# It willl return448, 452
#     # print(mystr[448:452])# It will give us fass

# patt2 = re.compile(r'.adm')
patt2 = re.compile(r'^adm')#String doesn't start with adm soo it didn't return anything
patt2 = re.compile(r'^Tata')# Mystr starts with Tata so for loop will print the object
patt2 = re.compile('$Tata')
patt2 = re.compile('ii$')
patt2 = re.compile('ai*')# a ho ya a ke baad kitne bhi i ho
patt2 = re.compile('ai+')# a ke baad minimum 1 i ho
patt2 = re.compile('ai{2}')# Exactly 2 i
patt2 = re.compile('(ai){2}')# aiai - kaha kaha hai
patt2 = re.compile(r'ai{1} | t')
patt2 = re.compile(r'ai{1} | FAX')

# Special Sequence

patt2 = re.compile(r'\ATata')
patt2 = re.compile(r'\bFAX')# Starting with FAX
patt2 = re.compile(r'Fax\b')#Ending with FAX
patt2 = re.compile(r'27\b')
patt2 = re.compile(r'\d{5}-\d{4}')
patt2 = re.compile(r',\Z')

"""Task"""

# patt2 = re.compile(r'\W{1}91\d{10}')


match2 = patt2.finditer((mystr))
for match in match2:
    print(match)







