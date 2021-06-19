from sense_hat import SenseHat
import requests

url = "https://athena.sabah.io/weather/kota-kinabalu.json"

r = requests.get(url = url)

data = r.json()

temp = data["current"]["temp"]
feel_like = data["current"]["feels_like"]
hum = data["current"]["humidity"]

print(temp)
print(feel_like)
print(hum)

sense = SenseHat()
sense.show_message(str(temp) + "C")