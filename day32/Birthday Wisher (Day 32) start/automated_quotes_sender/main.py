# import smtplib

# my_email = "gabyugarte1907@gmail.com"
# password = "wwlbhmfsiasbykaf"
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs="gabyugarte91@yahoo.com", 
#         msg="Subject:Hello\n\nThis is the body of my email."
#         )

# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(year)
# print(month)
# print(day_of_week)

# date_of_birth = dt.datetime(year= 1984, month= 11, day= 7, hour= 12)
# print(date_of_birth)

import smtplib
import datetime as dt
import random

MY_EMAIL = "gabyugarte1907@gmail.com"
MY_PASSWORD = "wwlbhmfsiasbykaf"


now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs="gabrielaugartemaco@gmail.com",
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )