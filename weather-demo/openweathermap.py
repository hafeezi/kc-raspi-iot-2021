import requests

api_key = "71a207eea0e16025540eda1430bc32d0"
url = "https://api.openweathermap.org/data/2.5/weather"
params = {'q': 'Kota Kinabalu', 'appid': api_key }

r = requests.get(url = url, params = params)

data = r.json()

temp = data['main']['temp'] - 273

print(temp)

