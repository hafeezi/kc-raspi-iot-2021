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
    data = request.json
    now = datetime.now()

    store.append({"temp": data["temp"], "dt": now})

    return "Data stored"
  else:
    index = len(store) - 1
    data = store[index]
    print(data)
    return jsonify(data)

@app.route("/db")
def show_store():
  return store
