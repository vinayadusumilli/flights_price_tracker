import ast
import requests
from dotenv import dotenv_values

config = {
    **dotenv_values(".env.shared"),
    **dotenv_values(".env.secret")
}

SHEETY_HOST_DOMAIN = "https://api.sheety.co/"
SHEETY_ENDPOINT = "/flightDeals/prices"
SHEETY_ENDPOINT_URL = f"{SHEETY_HOST_DOMAIN}{config['MY_SHEETY_API']}{SHEETY_ENDPOINT}"


class DataManager:
    def __init__(self):
        self.api_key = config["MY_SHEETY_API_KEY"]
        self.destination_data = {}

    def get_destination_data(self):
        header = {
            "Authorization": self.api_key
        }
        response = requests.get(url=SHEETY_ENDPOINT_URL, headers=header)
        self.destination_data = response.json()["prices"]

        """with open("data.txt") as file_data:
            data = file_data.read()
            data = ast.literal_eval(data)"""
        return self.destination_data


    def update_iata_code(self):
        header = {
            "Authorization": self.api_key
        }
        for each_data in self.destination_data:
            new_data = {
                "price":{
                    "iataCode": each_data["iataCode"]
                }
            }
            response = requests.post(
                url=f"{SHEETY_ENDPOINT_URL}/{each_data['id']}",
                headers=header,
                json=new_data
            )
            print(response.text)


