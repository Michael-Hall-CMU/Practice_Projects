import pandas
from datetime import datetime
import random
import smtplib

MY_EMAIL = "example@gmail.com"
MY_PASSWORD = "some_app_password"
SMTP_TAG = "smtp.gmail.com"

# Can automate the sender on the cloud to run every day using tasks on 'pythonanywhere' or another service

birthdays_file = pandas.read_csv("birthdays.csv")
birthdays_data = birthdays_file.to_dict(orient="records")

today = datetime.now()
year = today.year
month = today.month
day = today.day

for birthday in birthdays_data:
    if birthday["month"] == month and birthday["day"] == day:
        letter_number = random.randint(1,3)
        with open(f"./letter_templates/letter_{letter_number}.txt") as letter_file:
            letter = letter_file.read()
            new_letter = letter.replace("[NAME]", birthday["name"], -1)

        try:
            with smtplib.SMTP_SSL(SMTP_TAG) as connection:
                connection.login(MY_EMAIL, MY_PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs=birthday["email"],
                                    msg=f"Subject:Happy {year - birthday['year']} Birthday!\n\n{new_letter}")
            print(f"Email sent to {birthday['email']}")
        except Exception as exception:
            print(f"Email failed to send due to: {exception}")


# Alternative method:
# today = datetime.now()
# today_tuple = (today.month, today.day, today.year)
#
# data = pandas.read_csv("birthdays.csv")
#
# birthdays_dict = {(data_row["month"], data_row["day"]): data_row
#                   for (index, data_row) in data.iterrows()}
#
# if today_tuple in birthdays_dict:
#     birthday_person = birthdays_dict[today_tuple].......
