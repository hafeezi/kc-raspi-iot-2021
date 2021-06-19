from sense_hat import SenseHat
import requests


sense = SenseHat()
temp = sense.get_temperature() + "C"

url = "http://192.168.0.15:5000/temperature"

data = {"temp": temp}

r = requests.post(url = url, data = data)

print(r.text)