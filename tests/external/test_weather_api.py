import os
import json
import requests

with open(os.path.dirname(__file__) + "/../../config.json") as config_file:
    config = json.load(config_file)

api_key = config["current_weather"]["api_key"]
lat = config["current_weather"]["lat"]
lon = config["current_weather"]["lon"]
units = config["current_weather"]["units"]
url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&\
    exclude=hourly,daily&appid=%s&units=%s" % (lat, lon, api_key, units)
response = requests.get(url)
data = json.loads(response.text)

def test_weather_api_status() -> None:
    assert response.status_code == 200

def test_weather_api_type() -> None:
    assert isinstance(data, dict)

def test_weather_api_noapikey() -> None:
    api_key = ""
    units = config["current_weather"]["units"]
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&\
        exclude=hourly,daily&appid=%s&units=%s" % (lat, lon, api_key, units)
    response = requests.get(url)
    data = json.loads(response.text)
    assert data['cod'] == 401

def test_weather_api_locationerror() -> None:
    lat = 91.0 #Range of latitude from -90 to 90
    lon = 181.0 #Range of longitude from -180 to 180
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&\
        exclude=hourly,daily&appid=%s&units=%s" % (lat, lon, api_key, units)
    response = requests.get(url)
    data = json.loads(response.text)
    assert data['cod'] == '400'

def test_weather_api_invalidunit() -> None:
    units = "invalidunit"
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&\
        exclude=hourly,daily&appid=%s&units=%s" % (lat, lon, api_key, units)
    response = requests.get(url)
    data = json.loads(response.text)
    assert response.status_code == 200 
    #Units are set to 'standard' by default there the api should return data normally
