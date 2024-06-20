import os
from twilio.rest import Client
import smtplib


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.email = os.environ['MY_EMAIL']
        self.password = os.environ['MY_EMAIL_PASSWORD']
        self.twilio_virtual_number = os.environ['TWILIO_PHONE_NUM']
        self.twilio_verified_number = os.environ['TWILIO_VERIFIED_NUM']
        self.client = Client(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN'])
        self.connection = smtplib.SMTP_SSL(os.environ['SMTP_TAG'])

    def send_sms(self, message_body):
        message = self.client.messages.create(
            body=message_body,
            from_=self.twilio_virtual_number,
            to=self.twilio_verified_number
        )
        print(f"Sent message: {message.sid}")

    def send_emails(self, email_list, email_body):
        try:
            with self.connection:
                self.connection.login(user=self.email, password=self.password)
                for email in email_list:
                    self.connection.sendmail(
                        from_addr=self.email,
                        to_addrs=email,
                        msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode('utf-8')
                    )
                print("Sent the email")
        except Exception as exception:
            print(f"Failed to send email: {exception}")
