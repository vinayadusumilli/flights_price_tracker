import requests
import time
from dotenv import dotenv_values
from flight_data import FlightData

config = {
    **dotenv_values(".env.shared"),
    **dotenv_values(".env.secret")
}

TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v1/shopping/flight-offers"

class FlightSearch:
    def __init__(self, flight_data: FlightData) -> None:
        self.flight_data = flight_data
        self.api_key = config["MY_AMADEUS_API_KEY"]
        self.secret_key = config["MY_AMADEUS_SECRET_KEY"]
        self._token = self.get_new_token()

    def get_new_token(self):
        header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        body = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.secret_key
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)
        # New bearer token. Typically expires in 1799 seconds (30min)
        print(f"Your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()['access_token']

    def get_iata_code(self, city_name):
        header = {
            "Authorization": f"Bearer {self._token}"

        }
        query = {
            "keyword": city_name,
            "include": "AIRPORTS",
            "max": "2"

        }
        response = requests.get(url=IATA_ENDPOINT, headers=header, params=query)
        return response.json()["data"][0]["iataCode"]

    def get_cheap_flight(self):
        header = {
            "Authorization": f"Bearer {self._token}"

        }
        query = {
            "originLocationCode": self.flight_data.origin_location_code,
            "destinationLocationCode": "",
            "departureDate": "",
            "returnDate": "",
            "adults": 1,
            "travelClass": "ECONOMY",
            "nonStop": True,
            "currencyCode": "GBP",
            "maxPrice": 500,
            "max": 10

        }
        response = requests.get(url=FLIGHT_ENDPOINT, headers=header, params=query)
        return response.json()

