import requests
import datetime as dt

KIWI_ENDPOINT_SEARCH = "https://api.tequila.kiwi.com/search"
KIWI_KEY = ""



class FlightData:
    pass

    # def get_flight_prices(self, fly_from, fly_to):
    #     todays_date = dt.datetime.now().strftime("%d/%m/%Y")
    #     header = {
    #         "apikey": KIWI_KEY
    #     }
    #
    #     params_data = {
    #         "fly_from": fly_from,
    #         "fly_to": fly_to,
    #
    #     }
    #     response = requests.get()


fly_from ="MUC"
fly_to = "JNB"
now = dt.datetime.now()
todays_date = now.strftime("%d/%m/%Y")
date_60_days = (now + dt.timedelta(days=6*30)).strftime("%d/%m/%Y")

return_date_from = (now + dt.timedelta(days=7)).strftime("%d/%m/%Y")
return_date_to = (now + dt.timedelta(days=35)).strftime("%d/%m/%Y")
print(todays_date)
print(date_60_days)
print(return_date_from)
print(return_date_to)
header = {
    "apikey": KIWI_KEY
}

params_data = {
    "fly_from": fly_from,
    "fly_to": fly_to,

}
# response = requests.get()