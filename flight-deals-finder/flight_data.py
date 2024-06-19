class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date


def find_cheapest_flight(data):
    if data is None or not data['data']:
        print("No flight data")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")

    first_flight = data['data'][0]
    lowest_price = float(first_flight['price']['grandTotal'])
    cheapest_flight = get_flight_data(first_flight, lowest_price)

    for flight in data['data']:
        price = float(flight['price']['grandTotal'])
        if price < lowest_price:
            lowest_price = price
            cheapest_flight = get_flight_data(flight, lowest_price)
            print(f"Lowest price to {cheapest_flight.destination_airport} if ${lowest_price}")

    return cheapest_flight


def get_flight_data(flight, lowest_price):
    origin = flight['itineraries'][0]['segments'][0]['departure']['iataCode']
    destination = flight['itineraries'][0]['segments'][0]['arrival']['iataCode']
    out_date = flight['itineraries'][0]['segments'][0]['departure']['at'].split("T")[0]
    return_date = flight['itineraries'][1]['segments'][0]['departure']['at'].split("T")[0]

    return FlightData(lowest_price, origin, destination, out_date, return_date)
