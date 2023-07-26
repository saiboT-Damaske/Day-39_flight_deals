import requests

KIWI_ID = ""
KIWI_ENDPOINT_LOCATION = "https://api.tequila.kiwi.com/locations/query"
KIWI_KEY = ""


class FlightSearch:


    def get_destination_code(self, city_name):

        header = {
            "apikey": KIWI_KEY
        }

        search_data = {
            "term": city_name,
            "location_types": "city",
        }
        print(city_name)
        response = requests.get(url=KIWI_ENDPOINT_LOCATION, headers=header, params=search_data)
        city_iata_code = response.json()["locations"][0]["code"]
        print(city_iata_code)

        return city_iata_code

