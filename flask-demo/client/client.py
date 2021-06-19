from sense_hat import SenseHat
import requests
import time

url = "http://192.168.0.15:5000/temperature"

sense = SenseHat()

for x in range(0, 11):
  temp = sense.get_temperature() + "C"

  data = {"temp": temp}

  r = requests.post(url = url, data = data)

  print(r.text)

  time.sleep(60)

