import bs4
import urllib.request
import smtplib
import time
import pandas as pd

prices_list = []

def check_price():
    url = 'https://www.amazon.in/Fire-Boltt-Bluetooth-Headphones-Lightweight-Assistance/dp/B0814GJNKG/ref=sr_1_2_sspa?crid=15D92MMSGLI93&dchild=1&keywords=over%2Bthe%2Bear%2Bheadphone&qid=1627019145&sprefix=over%2Bthe%2Caps%2C377&sr=8-2-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExTlgzUTFRWDRFNjM3JmVuY3J5cHRlZElkPUEwMTgxMDM2OEczU1QxOEoxWlVGJmVuY3J5cHRlZEFkSWQ9QTA5MDcwMzhMRlZJTFI3WjlGOTQmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl&th=1'

    sauce = urllib.request.urlopen(url).read()
    soup = bs4.BeautifulSoup(sauce, "html.parser")

    prices = soup.find(id="priceblock_ourprice").get_text()
    prices = float(prices.replace(",", "").replace("₹", ""))
    prices_list.append(prices)
    return prices

def send_email(message):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("saggarwal.1709@gmail.com", "saksham1709")
    s.sendmail("saggarwal.1709@gmail.com", "1709.saksham@gmail.com", message)
    s.quit()

def price_decrease_check(price_list):
    if prices_list[-1] < prices_list[-2]:
        return True
    else:
        return False



count = 1
while True:
    current_price = check_price()
    if count > 1:
        flag = price_decrease_check(prices_list)
        if flag:
            decrease = prices_list[-1] - prices_list[-2]
            message = f"The price has decrease please check the item. The price decrease by {decrease} rupees."
            send_email(message) #ADD THE OTHER AGRUMENTS sender_email, sender_password, receiver_email
    time.sleep(43200)
    count += 1