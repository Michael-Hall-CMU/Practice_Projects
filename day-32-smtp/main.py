import datetime as dt
import random
import smtplib

MY_EMAIL = "example@gmail.com"
MY_PASSWORD = "some_app_password"
SMTP_TAG = "smtp.gmail.com"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    try:
        with smtplib.SMTP_SSL(SMTP_TAG) as connection:
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="destination_example@myyahoo.com",
                                msg=f"Subject:Monday Motivation\n\n{quote}")
        print("Sent the email")
    except Exception as exception:
        print(f"Failed to send email: {exception}")