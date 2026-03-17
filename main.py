import datetime as dt
import random
import smtplib
import pandas
import os

now = dt.datetime.now()
today = (now.month,now.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {
    (data_row.month, data_row.day): data_row
        for (index,data_row) in data.iterrows()
}

my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")

if today in birthdays_dict:

    birthday_person = birthdays_dict[today]
    name = birthday_person["name"]
    email = birthday_person["email"]

    rand_value = random.randint(1,3)

    with open(f"letter_templates/letter_{rand_value}.txt") as letter_file:
        letter = letter_file.read()
        letter = letter.replace("[NAME]", name)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f"Subject:Happy Birthday\n\n{letter}"
        )
