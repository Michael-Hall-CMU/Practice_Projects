import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
SHEETY_PRICES_ENDPOINT = os.environ['SHEETY_PRICES_ENDPOINT']


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.authorization = {
            "authorization": f"Bearer {os.environ['SHEETY_TOKEN']}"
        }
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(SHEETY_PRICES_ENDPOINT, headers=self.authorization)
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
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=self.authorization
            )
            print(response.text)
