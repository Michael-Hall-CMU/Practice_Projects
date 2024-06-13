import os
import requests
from datetime import datetime

USERNAME = os.environ['PIXELA_USERNAME']
TOKEN = os.environ['PIXELA_TOKEN']
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# # Signs up for a user account
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# # Creates a habit tracking graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# today = datetime(year=2024, month=6, day=12).strftime("%Y%m%d") # if you want to set a specific day
today = datetime.now().strftime("%Y%m%d") # formatted in yyyyMMdd

pixel_data = {
    "date": today,
    "quantity": "10.34",
}

# # Creates a pixel for the day on the graph
# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)


update_endpoint = f"{pixel_creation_endpoint}/{today}"

new_pixel_data = {
    "quantity": "20.34"
}

# # Updates a pixel for specified day on graph
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixel_creation_endpoint}/{today}"

# # Deletes a pixel for specified day on graph
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
