import requests


SHEETY_ENDPOINT = ""


class DataManager:

    # This class is responsible for talking to the Google Sheet.
    def __init__(self):

        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        response.raise_for_status()
        self.destination_data = response.json()["prices"]

        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=new_data)
            response.raise_for_status()
            print(response.text)

