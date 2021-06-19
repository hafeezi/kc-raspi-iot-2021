from sense_hat import SenseHat
import requests
from decimal import *

api_key = "YOUR API KEY"
url = "https://api.openweathermap.org/data/2.5/weather"
params = {'q': 'Kota Kinabalu', 'appid': api_key }

r = requests.get(url = url, params = params)

data = r.json()

temp_float = data['main']['temp'] - 273

temp = str(Decimal(temp_float)) + "C"

sense = SenseHat()
sense.show_message(temp)

