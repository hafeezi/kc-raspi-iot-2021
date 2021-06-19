from flask import Flask, request
from datetime import datetime

from flask.json import jsonify

app = Flask(__name__)

store = []

@app.route("/")
def hello_world():
  return "<p>Hello, World!</p>"

@app.route("/weather")
def weather():
  return "<p>This is the Weather Station</p>"

@app.route("/temperature", methods=["GET", "POST"])
def temperature():
  if request.method == "POST":
    data = request.get_json(force=True)
    now = datetime.now()
    print(data)

    temp = data["temp"]

    store.append({"temp": temp, "dt": now})

    return "Data stored"
  else:
    if len(store) > 0:
      index = len(store) - 1
      data = store[index]
      print(data)
      return jsonify(data)
    else:
      return "No Data"

@app.route("/db")
def show_store():
  return jsonify(store)
