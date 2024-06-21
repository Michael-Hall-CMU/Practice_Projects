import time
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

# ============================= Set up the Flight Search ===================

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "DFW"


# ============================= Update the Airport Codes in Google Sheet ===================

updated = False
# iata = International Air Transport Association code
for row in sheet_data:
    if row['iataCode'] == "":
        row['iataCode'] = flight_search.get_destination_code(row['city'])
        time.sleep(2)
        updated = True

if updated:
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

# ============================= Retrieve customer emails =====================
customer_data = data_manager.get_customer_emails()
customer_email_list = [row['whatIsYourEmail?'] for row in customer_data]

# ============================= Search for direct flights ===================

departure_date = datetime.now() + timedelta(days=(3 * 30)-5)
return_date = datetime.now() + timedelta(days=(3 * 30))

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination['iataCode'],
        from_time=departure_date,
        to_time=return_date
    )
    cheapest_flight = find_cheapest_flight(flights)
    print(f"Cheapest flight = {destination['city']}: ${cheapest_flight.price}")
    time.sleep(2)

    # ========================= Search for indirect flight if N/A ===================

    if cheapest_flight.price == "N/A":
        print(f"No direct flight to {destination['city']}. Looking for indirect flights...")
        stopover_flights = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination['iataCode'],
            from_time=departure_date,
            to_time=return_date,
            is_direct=False
        )
        cheapest_flight = find_cheapest_flight(flights)
        print(f"Cheapest flight = {destination['city']}: ${cheapest_flight.price}")

    # ========================= Send Notifications and Emails ===================

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination['lowestPrice']:
        if cheapest_flight.stops == 0:
            message = f"Low price alert! Only ${cheapest_flight.price} to fly direct "\
                      f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "\
                      f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        else:
            message = f"Low price alert! Only ${cheapest_flight.price} to fly " \
                      f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, " \
                      f"with {cheapest_flight.stops} stop(s) "\
                      f"departing on {cheapest_flight.out_date} and returning on {cheapest_flight.return_date}."

        print(f"Check your email. Lower price flight found to {destination['city']}!")
        # notification_manager.send_sms(message_body=message) # for sms if wanted

        # send emails to everyone on list
        notification_manager.send_emails(email_list=customer_email_list, email_body=message)
