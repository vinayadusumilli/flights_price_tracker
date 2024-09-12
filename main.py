from dotenv import dotenv_values

from flight_data import FlightData

SHEETY_HOST_DOMAIN = "https://api.sheety.co/"
SHEETY_ENDPOINT = "/flightDeals/prices"

config = {
    **dotenv_values(".env.shared"),
    **dotenv_values(".env.secret")
}

amadeus_api_key = config["MY_AMADEUS_API_KEY"]
amadeus_secret_key = config["MY_AMADEUS_SECRET_KEY"]
sheety_api = config["MY_SHEETY_API"]
sheety_api_key = config["MY_SHEETY_API_KEY"]

sheety_url = f"{SHEETY_HOST_DOMAIN}{sheety_api}{SHEETY_ENDPOINT}"

flightdata = FlightData(url=sheety_url, api_key=sheety_api_key)
flightdata.get_flight_data()