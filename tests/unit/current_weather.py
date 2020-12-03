import os
import json
import logging
import requests

with open(os.path.dirname(__file__) + "/../../config.json") as config_file:
    config = json.load(config_file)

def current_weather() -> str:
    """
    Returning the current weather conditions of preselected user locations.

    Weather conditions to be returned includes:
        - Temperature
        - Feels-Like Temperature
        - Humidity
        - Precipitation/ Special weather conditions
    User-defind variables includes:
        - Api key (obtained from https://openweathermap.org/appid)
        - User longitude, latitude (obtained from https://www.latlong.net/)
        - Units of measurement:
            - standard (temperature in Kelvin, wind speed in meter/sec)
            - metric (temperature in Celsius, wind speed in meter/sec)
            - imperial (temperature in Fahrenheit, wind speed in miles/hour)
    """
    api_key = config["current_weather"]["api_key"] #API key of the user
    lat = config["current_weather"]["lat"] #Latitude of location
    lon = config["current_weather"]["lon"] #Longitude of location
    units = config["current_weather"]["units"] #Units to use
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&\
        exclude=hourly,daily&appid=%s&units=%s" % (lat, lon, api_key, units)
    response = requests.get(url)
    data = json.loads(response.text)
    try:
        if data["cod"]: #Dictionary key "cod" appear if there is an error
            logging.error(str(data["message"]))
    except KeyError: #If key "cod" not found -> Normal
        temperature = data["current"]["temp"]
        feels_like = data["current"]["feels_like"]
        humidity = data["current"]["humidity"]
        precip = data["current"]["weather"][0]["main"]
        description = data["current"]["weather"][0]["description"].lower()
        precip_condition = ""
        if precip == "Thunderstorm":
            precip_condition = "there is currently a " + description + ". "
        elif precip == "Drizzle":
            precip_condition = "there is currently a " + description + ". "
        elif precip == "Rain":
            precip_condition = "there is currently a " + description + ". "
        elif precip == "Snow":
            precip_condition = "there is currently a " + description + ". "
        elif precip == "Clear":
            precip_condition = "is is currently clear outside. "
        elif precip == "Clouds":
            if data["current"]["weather"][0]["id"] == 801:
                precip_condition = "there are currently few clouds. "
            if data["current"]["weather"][0]["id"] == 802:
                precip_condition = "there are currently scattered clouds. "
            if data["current"]["weather"][0]["id"] == 803:
                precip_condition = "there are currently broken clouds. "
            if data["current"]["weather"][0]["id"] == 804:
                precip_condition = "the clouds are overcast currently. "
        elif precip == "Mist":
            precip_condition = "it is currently misty outside. "
        elif precip == "Smoke":
            precip_condition = "it is currently smoky outside. "
        elif precip == "Haze":
            precip_condition = "it is currently hazy outside. "
        elif precip == "Dust":
            precip_condition = "it is currently dusty outside, "\
                + "check the latest weather warning before you go out. "
        elif precip == "Fog":
            precip_condition = "it is currently foggy outside. "
        elif precip == "Sand":
            precip_condition = "it is currently sandy outside, "\
                + "check the latest weather warning before you go out. "
        elif precip == "Ash":
            precip_condition = "there are volcanic ash outside, "\
                + "check the latest weather warning before you go out. "
        elif precip == "Squall":
            precip_condition = "there are squalls outside, "\
                + "check the latest weather warning before you go out. "
        elif precip == "Tornado":
            precip_condition = "there is currently a tornado outside, "\
                + "check the latest weather warning before you go out. "
        else:
            precip_condition = "there are special weather conditions "\
                + "outside currently, check latest news before you go out. "
        output = "The current temperature is " + str(temperature)\
            + " degrees celsius, and it feels like " + str(feels_like)\
                + " degrees celsius. The humidity is " + str(humidity)\
                    + " percent currently. Additionally, "\
                        + str(precip_condition)
    weather_log = "Weather info fetched : " + str(output)
    logging.info(weather_log) #Logging the output of current weather
    return output
