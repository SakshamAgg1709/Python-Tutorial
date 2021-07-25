# Email Collector

import re

str = '''
BizzeOnline - Website Design and Development Company Gurgaon
HOME
SERVICES
TECHNOLOGIES
INDUSTRY WE SERVE
DISCOVER BIZZEONLINE
PORTFOLIO
CONTACT
CALL ANYTIME
+91-9643056057
website design company close button
HOME
SERVICES
TECHNOLOGIES
INDUSTRY WE SERVE
DISCOVER BIZZEONLINE
PORTFOLIO
CONTACT
BizzeOnline is a website design & development company in gurgaon haryana india - 122001

info@bizzeonline.com
+91-8178567042

CONTACT BIZZEONLINE
HOMECONTACT
OFFICES NEAR YOU.
INDIA
Gurgaon
info@bizzeonline.com
+91-8178567042
INDIA
Gwalior
info@bizzeonline.com
+91-8178567042     
INDIA
Delhi
info@bizzeonline.com
+91-8178567042
CANADA
Toronto
info@bizzeonline.com
+91-8178567042

WRITE US A MESSAGE.
Your Name
Email Address
Phone Number
Subject
Write Message

SEND MESSAGE
Call Now
bizzeonline website design company footer logo
Welcome to our website bizzeonline.com website design & development company
 
 
 
EXPLORE
Home
About
Meet Our Team
Our Portfolio
Contact
Career
Support
Privacy Policy
Terms Of Use
Help
CONTACT
359 Sector 28
Gurgaon HR. - 122001 India
+91-9643056057
info@bizzeonline.com
NEWSLETTER
Email Address

Sign up for our latest news & articles. We won’t give you spam mails.
© copyright 2020-21 | Website Design & Developed By  Bizzeonline
{"mode":"full","isActive":false}
'''

patt2 = re.compile(r'\S+@\S+')


match2 = patt2.finditer((str))

f = open("email.txt", 'wt')

for match in match2:
    print(match)
    li = list(match.span())
    span1 = li[0]
    span2 = li[1]
    f.write(f"Email - {str[span1:span2]}\n")


"""Harry's Bhai solution"""

"""First One is by Harry bhai and the others were of other participants"""

"""All three are working"""
email = re.findall(r"[0-9a-zA-Z._%]+@[0-9a-zA-Z._%]+[.][a-zA-Z.0-9]+", str)# It can be different for different email provider
email = re.findall(r'\w+@\S+\w' , str)
email = re.findall(r"[A-Za-z]{3,20}@[a-z]{2,12}.[a-z]{2,4}", str)
print(email)
