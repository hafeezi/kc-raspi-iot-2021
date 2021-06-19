from sense_hat import SenseHat
import requests
import time

url = "http://192.168.0.15:5000/temperature"

sense = SenseHat()

for x in range(0, 11):
  temp = round(sense.get_temperature(), 2)

  data = {"temp": str(temp) + "C"}

  r = requests.post(url = url, json = data)

  print(r.text)

  time.sleep(60)

