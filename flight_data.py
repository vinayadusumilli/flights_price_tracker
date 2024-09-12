from pprint import pprint

import requests


class FlightData:
    def __init__(self, **data):
        self.data = data
        self.url = self.data["url"]
        self.api_key = self.data["api_key"]
        self.headers = {
            "Authorization": self.api_key
        }

    def get_flight_data(self):
        response = requests.get(self.url, headers=self.headers)
        pprint(response.json())

