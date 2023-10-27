##################### Extra Hard Starting Project ######################
import random
import pandas
import smtplib
import datetime as dt

my_email = "muawan541@gmail.com"
password = "yrpd eawr mydz enqd"

# 1. Update the birthdays.csv

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("day-32-start/birthday-wisher-extrahard-start/birthdays.csv")
birthday_data = {(row.month, row.day ): row for (index, row) in data.iterrows()}
# 2. Check if today matches a birthday in the birthdays.csv

if today_tuple in birthday_data:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    birthday_person = birthday_data[today_tuple]
    letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
    with open(f"day-32-start/birthday-wisher-extrahard-start/letter_templates/letter_{random.randint(1,3)}.txt") as letter:
        letter = letter.read()
        new_letter = letter.replace("[NAME]", birthday_person["name"] )
    
# 4. Send the letter generated in step 3 to that person's email address.

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            to_addrs="heyyymuhammad@gmail.com",
            from_addr=my_email,
            msg=f"Subject: Happy Birthday\n\n{new_letter}"
        )




