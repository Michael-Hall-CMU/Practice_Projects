import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.prices_endpoint = os.environ['SHEETY_PRICES_ENDPOINT']
        self.users_endpoint = os.environ['SHEETY_USERS_ENDPOINT']
        self.authorization = {
            "authorization": f"Bearer {os.environ['SHEETY_TOKEN']}"
        }
        self.destination_data = {}
        self.customer_data = {}


    def get_destination_data(self):
        response = requests.get(self.prices_endpoint, headers=self.authorization)
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city['iataCode']
                }
            }

            response = requests.put(
                url=f"{self.prices_endpoint}/{city['id']}",
                json=new_data,
                headers=self.authorization
            )
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(self.users_endpoint, headers=self.authorization)
        data = response.json()
        self.customer_data = data['users']
        return self.customer_data
