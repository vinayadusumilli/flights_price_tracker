from pprint import pprint
import time
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch

data_manager = DataManager()
flight_data = FlightData()
flight_search = FlightSearch(flight_data)

sheet_data = data_manager.get_destination_data()
for flight_data in sheet_data:
    if flight_data["iataCode"] == "":
        iata_code = flight_search.get_iata_code(flight_data["city"])
        time.sleep(4)
        flight_data["iataCode"] = iata_code
pprint(f"sheet_data:\n {sheet_data}")
data_manager.destination_data = sheet_data
data_manager.update_iata_code()

