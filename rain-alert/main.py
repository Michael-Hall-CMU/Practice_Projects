import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

owm_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ['WEATHER_API_KEY']
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

weather_params = {
    "lat": 32.975540,
    "lon": -96.889793,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(owm_endpoint, weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data['list']:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True
        break

if will_rain:
    # proxy is for running on free pythonanywhere cloud
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_='twilio generated number',
        to='your verified number'
    )
    print(message.sid)