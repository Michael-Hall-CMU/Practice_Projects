import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 32.975540 # Your latitude
MY_LONG = -96.889793 # Your longitude
MY_EMAIL = "example@gmail.com"
MY_PASS = "some_app_password"
MY_SMTP = "smtp.gmail.com"


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    return MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    return time_now >= sunset or time_now <= sunrise


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        try:
            with smtplib.SMTP_SSL(MY_SMTP) as connection:
                connection.login(MY_EMAIL, MY_PASS)
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs=MY_EMAIL,
                                    msg="Subject:Look Up\n\nLook up now to see the ISS overhead")
            print("Email sent successfully")
        except Exception as exception:
            print(f"Email failed due to {exception}")
