import os
from twilio.rest import Client


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN'])

    def send_sms(self, message_body):
        message = self.client.messages.create(
            body=message_body,
            from_=os.environ['TWILIO_PHONE_NUM'],
            to=os.environ['MY_PHONE_NUM']
        )
        print(f"Sent message: {message.sid}")
