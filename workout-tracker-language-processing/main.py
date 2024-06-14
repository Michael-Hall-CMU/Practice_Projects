import os
import requests
from datetime import datetime

APP_ID = os.environ['NUTRITIONIX_APP_ID']
API_KEY = os.environ['NUTRITIONIX_API_KEY']
SHEET_TOKEN = os.environ['SHEET_TOKEN']
SHEET_ENDPOINT = os.environ['SHEET_ENDPOINT']

GENDER = "male"
WEIGHT_KG = 75
HEIGHT_CM = 180
AGE = 27

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(exercise_endpoint, json=params, headers=headers)
workout_res = response.json()

today = datetime.now()

sheet_headers = {
        "Authorization": f"Bearer {SHEET_TOKEN}",
    }

for workout in workout_res['exercises']:

    sheet_params = {
        "workout": {
            "date": today.strftime("%m/%d/%Y"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": workout['name'].title(),
            "duration": workout['duration_min'],
            "calories": workout['nf_calories'],
        }
    }

    sheet_response = requests.post(SHEET_ENDPOINT, json=sheet_params, headers=sheet_headers)
    print(sheet_response.text)
