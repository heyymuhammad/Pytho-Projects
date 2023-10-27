import random

with open(file="day-32-start/quotes.txt") as qt:
    qout_list = qt.readlines()
    new_quote = random.choice(qout_list)

import datetime as dt

now = dt.datetime.now()
week_day = now.weekday()

import smtplib

my_email = "muawan541@gmail.com"
password = "yrpd eawr mydz enqd"

if week_day:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs= "heyyymuhammad@gmail.com",
            msg=f"Subject: Motivation for Today\n{new_quote}"
        )
