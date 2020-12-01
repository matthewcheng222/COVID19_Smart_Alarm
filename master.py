"""
This Module is a program to integrate smart alarm features into an
HTML template using Flask. The features of the alarm include:
    - Basic alarm features (creating, modifying and deleting alarms)
    - Getting top news headlines for the day
    - Getting up-to-date local COVID figures
    - Getting current local weather conditions
"""
import json
import time
import sched
import logging
import datetime
from datetime import datetime
from time import strftime, localtime
from flask import Flask, render_template, request, redirect, Markup
from uk_covid19 import Cov19API
from newsapi import NewsApiClient
import pyttsx3
import requests

app = Flask(__name__)

with open("config.json") as config_file:
    config = json.load(config_file)
logging.basicConfig(filename = 'smart_alarm.log', encoding = "utf-8",\
    level = logging.DEBUG)
s = sched.scheduler(time.time, time.sleep)
alarms_list = []
alarm_list_sched = []
dismissed_alarms = []
notifications_list = []
dismissed_notifications = []

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
    api_key = config["current_weather"]["api_key"]
    lat = config["current_weather"]["lat"]
    lon = config["current_weather"]["lon"]
    units = config["current_weather"]["units"]
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&\
        exclude=hourly,daily&appid=%s&units=%s" % (lat, lon, api_key, units)
    response = requests.get(url)
    data = json.loads(response.text)
    try:
        if data["cod"]:
            message = data["message"]
            logging.error(message)
    except KeyError:
        temperature = data["current"]["temp"]
        feels_like = data["current"]["feels_like"]
        humidity = data["current"]["humidity"]
        precip = data["current"]["weather"][0]["main"]
        description = data["current"]["weather"][0]["description"]
        precip_condition = ""
        if precip == "Thunderstorm":
            precip_condition = "there is currently a " + description.lower() + ". "
        elif precip == "Drizzle":
            precip_condition = "there is currently a " + description.lower() + ". "
        elif precip == "Rain":
            precip_condition = "there is currently a " + description.lower() + ". "
        elif precip == "Snow":
            precip_condition = "there is currently a " + description.lower() + ". "
        elif precip == "Clear":
            precip_condition = "is is currently clear outside. "
        elif precip == "Clouds":
            if data["current"]["weather"][0]["id"] == 801:
                precip_condition = "there are currently few clouds outside. "
            if data["current"]["weather"][0]["id"] == 802:
                precip_condition = "there are currently scattered clouds. "
            if data["current"]["weather"][0]["id"] == 803:
                precip_condition = "there are currently broken clouds outside. "
            if data["current"]["weather"][0]["id"] == 804:
                precip_condition = "the clouds outside are overcast currently. "
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
                + "outside currently, check the latest news before you go out. "
        output = "The current temperature is " + str(temperature)\
            + " degrees celsius, and it feels like " + str(feels_like)\
                + " degrees celsius. The humidity is " + str(humidity)\
                    + " percent currently. Additionally, "\
                        + str(precip_condition)
    return output

def weather_notifications():
    """
    Appending weather notifications of the day to notifications list.

    The function takes data from Openweather and creates day-to-day weather
    notifications to the user. The content in the notifications include:
        daily_pop -- Probability of rain for the day (in percent)
        wind_speed, wind_deg -- direction and speed of wind currently (if
        wind speed is exceeds level of 'Fresh Breeze')
        temp_max, temp_min, daily_uvi -- maximum and minimum temperature of
        the day, along with the UV index during midday
    """
    api_key = config["current_weather"]["api_key"]
    lat = config["current_weather"]["lat"]
    lon = config["current_weather"]["lon"]
    units = config["current_weather"]["units"]
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&\
        exclude=hourly,daily&appid=%s&units=%s" % (lat, lon, api_key, units)
    response = requests.get(url)
    data = json.loads(response.text)
    try:
        if data["cod"]:
            message = data["message"]
            logging.error(message)
    except KeyError:
        current_wind_speed = data["current"]["wind_speed"]
        current_wind_deg = data["current"]["wind_deg"]
        daily = data["daily"]
        daily_temp_min = daily[0]["temp"]["min"]
        daily_temp_max = daily[0]["temp"]["max"]
        daily_uvi = daily[0]["uvi"]
        daily_pop = daily[0]["pop"]
        refresh_freq = config["current_weather"]["wx_refresh_frequency"]
        if current_wind_speed >= 10.5:
            if units == "metric":
                speed_unit = "meter/sec"
            if units == "standard":
                speed_unit = "meter/sec"
            if units == "imperial":
                speed_unit = "miles/hour"
            if 315 <= current_wind_deg < 360:
                wind_direction = "north"
            if 0 <= current_wind_deg < 45:
                wind_direction = "north"
            if 45 <= current_wind_deg < 135:
                wind_direction = "east"
            if 135 <= current_wind_deg < 225:
                wind_direction = "south"
            if 225 <= current_wind_deg < 315:
                wind_direction = "west"
            wind_notification = "The wind is currently "\
                + str(current_wind_speed) + " " + speed_unit\
                    + " coming from the " + str(wind_direction)
            wind_dictionary = {'title' : 'Current wind information',
            'content' : wind_notification}
            if wind_dictionary not in dismissed_notifications:
                if wind_dictionary not in notifications_list:
                    notifications_list.append(wind_dictionary)
        if daily:
            rain_probability = "The probably of raining today is "\
                + str(int(daily_pop*100)) + " percent. "
            rain_dictionary = {'title' : 'Rain Probability of today',
            'content' : rain_probability}
            if rain_dictionary not in dismissed_notifications:
                if rain_dictionary not in notifications_list:
                    notifications_list.append(rain_dictionary)
            daily_temp_uvi = "The maximum and minimum temperature today is "\
                + str(daily_temp_max) + " degrees celcius and "\
                    + str(daily_temp_min) + " degrees celcius respectively."\
                        + " The midday UV index is " + str(daily_uvi) + ". "
            temp_uvi_dictionary = {'title' : "Today's weather briefing",
            'content' : daily_temp_uvi}
            if temp_uvi_dictionary not in dismissed_notifications:
                if temp_uvi_dictionary not in notifications_list:
                    notifications_list.append(temp_uvi_dictionary)
    s.enter(refresh_freq, 1, weather_notifications, )

def uk_covid_announcement() -> str:
    """
    Returning the latest COVID-19 figures in user-defined local location.

    Returned figures include:
        - Last-updated date
        - Location
        - Daily new cases
        - Daily new deaths
        - Cumulative cases
        - Cumulative deaths

    User-defined variables include:
        - Area
    """
    area = str(config["covid19_api"]["area_name"])
    local = ['areaName={}'.format(area)]
    cases_and_deaths = {
        "date": "date",
        "areaName": "areaName",
        "cases": {
            "daily": "newCasesByPublishDate",
            "cumulative": "cumCasesByPublishDate"
        },
        "deaths": {
            "daily": "newDeathsByDeathDate",
            "cumulative": "cumDeathsByDeathDate"
        }
    }
    api = Cov19API(filters = local, structure = cases_and_deaths,
    latest_by="newCasesByPublishDate")
    get = api.get_json (as_string = True)
    data = json.loads(get)
    try:
        last_updated = data["lastUpdate"][:10]
        last_updated = datetime.strptime(last_updated, "%Y-%m-%d")
        last_updated = datetime.strftime(last_updated, "%A, %d %B, %Y")
        main = data["data"]
        new_day_cases = main[0]['cases']['daily']
        new_cum_cases = main[0]['cases']['cumulative']
        new_day_death = main[0]['deaths']['daily']
        new_cum_death = main[0]['deaths']['cumulative']
        if new_day_death is None:
            new_day_death_new = 0
        if new_cum_death is None:
            new_cum_death_new = 0
        output = "For COVID, as of " + str(last_updated) + ", there are "\
            + str(new_day_cases) + " new cases and "\
                + str(new_day_death_new) + " new death cases at " + area\
                    + ". There are " + str(new_cum_cases) + " cases and "\
                        + str(new_cum_death_new)\
                            + " death cases cumulatively. "
        return output
    except IsADirectoryError:
        logging.error("Error : The filename is not defined in the path")
    except ValueError:
        error = "Error : The filename does not end with the correct"\
            + "extension for the requested format"
        logging.error(error)

def uk_covid_notifications():
    """
    Appending the latest national COVID-19 figures of the UK to the list
    of notifications.
    """
    covid_refresh_freq = config["covid19_api"]["covid_refresh_frequency"]
    england_only = ['areaType=nation', 'areaName=England']
    cases_and_deaths = {
    "date": "date",
    "areaName": "areaName",
    "areaCode": "areaCode",
    "newCasesByPublishDate": "newCasesByPublishDate",
    "cumCasesByPublishDate": "cumCasesByPublishDate",
    }
    api = Cov19API(filters = england_only, structure = cases_and_deaths,
    latest_by="newCasesByPublishDate")
    get = api.get_json (as_string = True)
    data = json.loads(get)
    try:
        last_updated = data["lastUpdate"][:10]
        last_updated = datetime.strptime(last_updated, "%Y-%m-%d")
        last_updated = datetime.strftime(last_updated, "%A, %d %B, %Y")
        new_day_cases = data['data'][0]['newCasesByPublishDate']
        new_cum_cases = data['data'][0]['cumCasesByPublishDate']
        covid_dictionary = {'title' : 'Latest COVID-19 cases in the UK',
        'content' : 'There are ' + str(new_day_cases)\
            + ' new COVID cases on ' + str(last_updated)\
                + '. There are totally now ' + str(new_cum_cases)\
                    + ' COVID cases in the UK.'}
    except IsADirectoryError:
        logging.error("Error : The filename is not defined in the path")
    except ValueError:
        error = "Error : The filename does not end with the correct"\
            + "extension for the requested format"
        logging.error(error)
    if covid_dictionary not in dismissed_notifications:
        if covid_dictionary not in notifications_list:
            notifications_list.append(covid_dictionary)
    s.enter(covid_refresh_freq, 1, uk_covid_notifications, )

def top_news_titles() -> str:
    """
    Returning titles of top news stories (for announcement):

    User-defined variables include:
        - Number of news stories to return
    """
    api = config["news"]["api_key"]
    language = config["news"]["language"]
    newsapi = NewsApiClient (api_key = api)
    top_headlines = newsapi.get_top_headlines (language = language)
    if top_headlines["status"] == "ok":
        articles = top_headlines["articles"]
        results = []
        to_export = config["news"]["no_of_news"]
        for sources in articles:
            results.append(sources["title"])
        news_list = results[0:to_export]
        news_join = ", "
        news_join = news_join.join(news_list)
        output = "Here are the top " + str(to_export)\
            + " news story titles for today: " + news_join
    elif top_headlines["status"] == "error":
        error_output = "Error : " + top_headlines["code"] + " - "\
            + top_headlines["message"]
        logging.error(error_output)
    return output

def top_news_details() -> dict:
    """
    Appending titles and details of top news stories to notifications_list:

    This function will take titles and description of top news stories and
    adding them to notifications_list in the format of a dictionary

    The dictionary take the format of : {'title':title, 'content':content}
    User-defined variables include:
        - Number of news stories to return
    """
    newsapi = NewsApiClient (api_key = config["news"]["api_key"])
    top_headlines = newsapi.get_top_headlines (language = config["news"]["language"])
    refresh_freq = config["news"]["news_refresh_frequency"]
    if top_headlines["status"] == "ok":
        articles = top_headlines["articles"]
        results = []
        to_export = config["news"]["no_of_news"]
        for entry in articles[0:to_export]:
            details = {key: entry[key] for key in entry.keys() & {'title', 'description', 'url'}}
            results.append(details)
        for details in results:
            title = details['title']
            url = details['url']
            url_link = "(Click " + Markup("<a href='%s'>Here</a>") % (url) + " to learn more.)"
            content = Markup("%s <br> %s") % (details['description'], url_link)
            dictionary = {'title' : title, 'content' : content}
            if dictionary not in dismissed_notifications:
                if dictionary not in notifications_list:
                    notifications_list.append(dictionary)
    elif top_headlines["status"] == "error":
        error_output = "Error : " + top_headlines["code"] + " - "\
            + top_headlines["message"]
        logging.error(error_output)
    s.enter(refresh_freq, 1, top_news_details, )

def announcement(alarm_label : str, announcement_type : str) -> None:
    """
    Using pyttsx3 to read out announcements (triggered by alarms).

    Keyword Arguments:
    announcement_type -- User-selected components for the announcement
        a. weather_only (time, current weather, local COVID-19 figures)
        b. news_only (time, local COVID-19 figures, top news stories)
        c. news_and_weather (time, current weather, local COVID-19 figures, top news stories)
    """
    if int(strftime("%H", localtime())) >6 and int(strftime("%H", localtime())) <= 11:
        greeting = "Good Morning, "
    if int(strftime("%H", localtime())) > 11 and int(strftime("%H", localtime())) <= 18:
        greeting = "Good Afternoon, "
    if int(strftime("%H", localtime())) > 18 and int(strftime("%H", localtime())) < 23:
        greeting = "Good Evening, "
    else:
        greeting = "Hello, "
    time_briefing = " the time now is " + strftime("%H:%M", localtime())\
        + " and it is the time of your alarm '" + alarm_label + "'. "
    weather_briefing = current_weather()
    covid_briefing = uk_covid_announcement()
    news_briefing = top_news_titles()
    announcement_default = greeting + time_briefing + weather_briefing\
        + covid_briefing + news_briefing
    announcement_with_weather = greeting + time_briefing + weather_briefing\
        + covid_briefing
    announcement_with_news = greeting + time_briefing + covid_briefing\
        + news_briefing
    if announcement_type == "weather_only":
        briefing = announcement_with_weather
    elif announcement_type == "news_only":
        briefing = announcement_with_news
    elif announcement_type == "news_and_weather":
        briefing = announcement_default
    engine = pyttsx3.init()
    engine.setProperty("rate", 165)
    try:
        engine.endLoop()
    except RuntimeError:
        error = "PyTTSx3 Endloop error detected - Program allowed to"\
            + " continue without adjustment."
        logging.error(error)
    engine.say(briefing)
    engine.runAndWait()
    for entry in alarms_list:
        if entry['title'] == alarm_label:
            alarms_list.remove(entry)
    for alarms in alarm_list_sched:
        if alarms['alarm_label'] == alarm_label:
            alarm_list_sched.remove(alarms)
    log_info = "Alarm Triggered : " + briefing
    logging.info(log_info)

def alarm(alarm_datetime, alarm_label, with_news, with_weather):
    """
    Creating alarms using user input of the form.

    The function adds the alarm to alarms_list, which creates a widget on the
    alarm section of the HTML template.

    The function converts the input to time difference in seconds, and then
    adding the alarm into a schedule list in the format of the sched module.

    Keyword Arguments:
    alarm_datetime -- The date and time for the alarm to be created
    alarm_label -- The name of the alarm
    with_news -- Whether news should be included in the announcement
    with_weather -- Whether weather should be included in the announcement
    """
    current_time = datetime.strptime(datetime.now().strftime\
        ("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
    alarm_time = alarm_datetime[0:10] + " " + alarm_datetime[11:16]
    time_alarm = datetime.strptime(alarm_time, "%Y-%m-%d %H:%M")
    time_delay = time_alarm - current_time
    time_delay_sec = int(time_delay.total_seconds())
    if with_news == 'news' and with_weather == 'weather':
        content = "Your alarm is set at " + str(time_alarm) + " with time,"\
            + " weather, COVID and news announcements. (Created at " +\
                str(current_time) + ")"
        announcement_type = "news_and_weather"
    elif with_news == 'news':
        content = "Your alarm is set at " + str(time_alarm) + " with time,"\
            + " COVID and news announcements. (Created at " +\
                str(current_time) + ")"
        announcement_type = "news_only"
    elif with_weather == 'weather':
        content = "Your alarm is set at " + str(time_alarm) + " with time,"\
            + " weather and COVID announcements. (Created at " +\
                str(current_time) + ")"
        announcement_type = "weather_only"
    else:
        content = "Your alarm is set at " + str(time_alarm) + " with"\
            + " default announcements. (Created at " +\
                str(current_time) + ")"
        announcement_type = "news_and_weather"
    title = alarm_label
    alarm_dictionary = {'title' : title, 'content' : content}
    alarm_sched_directory = {'alarm_label':alarm_label,
    'time_delay_sec':time_delay_sec,
    'announcement_type':announcement_type,
    'id_key':str("alarm_" + str(title) + "_for_time" + str(time_alarm))}
    if alarm_dictionary not in alarms_list:
        alarms_list.append(alarm_dictionary)
    alarm_list_sched.append(alarm_sched_directory)
    run_alarm(alarm_label)
    logging.info(alarm_list_sched)
    logging.info(alarm_dictionary)

def run_alarm(alarm_label : str):
    """
    Adding the created alarm into the scheduler.

    The function takes input alarm_label and reads the information about
    the alarm from the list alarm_list_sched, which consist of name of
    alarm, time difference between now and the alarm, type of announcement
    to be announced, and the time of creation of the alarm. The function
    then add the alarm into the schedulerusing the sched module.

    Keyword Arguments:
        alarm_label -- The name of the alarm to be added to the scheduler
    """
    for alarms in alarm_list_sched:
        if alarms['alarm_label'] == alarm_label:
            priority = alarm_list_sched.index(alarms) + 1
            alarm_label = alarms['alarm_label']
            time_delay = alarms['time_delay_sec']
            announcement_type = alarms['announcement_type']
            alarms['id_key'] = s.enter(time_delay, priority, announcement,\
                kwargs={'alarm_label' : alarm_label,\
                    'announcement_type' : announcement_type})
            logging.info(s.queue)

@app.route('/')
def redirect_to_index():
    """
    Redirecting users who visit 127.0.0.1:5000/ to the /index page.
    """
    return redirect('index')

@app.route('/index', methods = ["GET", "POST"])
def index():
    """
    Formatting and assembling functions to the HTML template.

    The function gets input of users from the HTML template and assigns them
    into functions. Variables of user input includes:
        alarm_label -- Label of the alarm
        alarm_datetime -- Date and time of the alarm
        with_news -- Whether the announcement includes news briefing
        with_weather -- Whether the announcement includes weather briefing
        remove_alarms -- Label of the alarm to be dismissed
        remove_notifications -- Title of the notifications to be dismissed
    """
    s.run(blocking=False)
    page_title = Markup("ECM1400 CA3 <br> COVID_19 Smart Alarm")
    favicon = "/static/favicon.ico"
    image = "image.jpg"
    top_news_details()
    weather_notifications()
    uk_covid_notifications()
    remove_alarms = request.args.get("alarm_item")
    remove_notifications = request.args.get("notif")
    alarm_datetime = request.args.get("alarm")
    alarm_label = request.args.get("two")
    with_news = request.args.get("news")
    with_weather = request.args.get("weather")
    if alarm_datetime:
        current_time = datetime.strptime(datetime.now().strftime\
        ("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
        alarm_time = alarm_datetime[0:10] + " " + alarm_datetime[11:16]
        time_alarm = datetime.strptime(alarm_time, "%Y-%m-%d %H:%M")
        if time_alarm > current_time:
            alarm(alarm_datetime, alarm_label, with_news, with_weather)
            return redirect('/index')
        logging.error("Alarm not created : Alarm is not in the future")
        return redirect('/index')
    if remove_alarms:
        for entry in alarms_list:
            if entry['title'] == remove_alarms:
                alarms_list.remove(entry)
                dismissed_alarms.append(entry)
                for alarms in alarm_list_sched:
                    if alarms['alarm_label'] == remove_alarms:
                        id_key = alarms['id_key']
                        s.cancel(id_key)
                return redirect('/index')
    if remove_notifications:
        for entry in notifications_list:
            if entry['title'] == remove_notifications:
                notifications_list.remove(entry)
                dismissed_notifications.append(entry)
                log_info = "News article '" + remove_notifications\
                    + "' is dismissed and removed from notifications_list"
                logging.info(log_info)
                return redirect('/index')
    return render_template('index.html', title = page_title,\
        favicon = favicon, image = image,\
            notifications = notifications_list, alarms = alarms_list)

if __name__ == "__main__":
    app.run()
