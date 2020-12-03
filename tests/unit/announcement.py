import os
import json
import logging
from time import strftime, localtime
from current_weather import current_weather
from uk_covid_announcement import uk_covid_announcement
from top_news_titles import top_news_titles
import pyttsx3

with open(os.path.dirname(__file__) + "/../../config.json") as config_file:
    config = json.load(config_file)

alarms_list = []
alarm_list_sched = []

def announcement(alarm_label : str, announcement_type : str) -> None:
    """
    Using pyttsx3 to read out announcements (triggered by alarms).

    Keyword Arguments:
    announcement_type -- User-selected components for the announcement
        a. weather_only (time, weather, local COVID-19 figures)
        b. news_only (time, local COVID-19 figures, top news)
        c. news_and_weather (time, weather, local COVID-19 figures, top news)
    """
    if int(strftime("%H", localtime())) >6 and\
        int(strftime("%H", localtime())) <= 11:
        greeting = "Good Morning, "
    if int(strftime("%H", localtime())) > 11 and\
        int(strftime("%H", localtime())) <= 18:
        greeting = "Good Afternoon, "
    if int(strftime("%H", localtime())) > 18 and\
        int(strftime("%H", localtime())) < 23:
        greeting = "Good Evening, "
    else:
        greeting = "Hello, "
    time_briefing = " the time now is " + strftime("%H:%M", localtime())\
        + " and it is the time of your alarm '" + alarm_label + "'. "
    weather_briefing = current_weather()
    #Calling function for weather announcement
    covid_briefing = uk_covid_announcement()
    #Calling function for CVID-19 announcement
    news_briefing = top_news_titles()
    #Calling function for news titles announcement
    announcement_default = greeting + time_briefing + covid_briefing
    announcement_with_weather = greeting + time_briefing + weather_briefing\
        + covid_briefing
    announcement_with_news = greeting + time_briefing + covid_briefing\
        + news_briefing
    announcement_news_weather = greeting + time_briefing + weather_briefing\
        + covid_briefing + news_briefing
    if announcement_type == "weather_only": #Setting announcement type
        briefing = announcement_with_weather
    elif announcement_type == "news_only": #Setting announcement type
        briefing = announcement_with_news
    elif announcement_type == "news_and_weather": #Setting announcement type
        briefing = announcement_news_weather
    elif announcement_type == "announcement_default":
        briefing = announcement_default
    engine = pyttsx3.init() #Initializing the PyTTSx3 engine
    speak_rate = config["pyttsx3"]["speak_rate"]
    engine.setProperty("rate", speak_rate) #Setting the PyTTSx3 engine's speak rate
    try:
        engine.endLoop() #Ending the PyTTSx3 loop if it is running
    except RuntimeError:
        error = "PyTTSx3 Endloop error detected - Program allowed to"\
            + " continue without adjustment."
        logging.error(error) #Logging error if Endloop error detected
    engine.say(briefing) #Setting content for PyTTSx3 engine to say
    engine.runAndWait() #Running PyTTSx3 engine
    for entry in alarms_list:
        if entry['title'] == alarm_label:
            alarms_list.remove(entry)
            #Removing entry from alarms_list (Alarm widget) when alarm trigger
    for alarms in alarm_list_sched:
        if alarms['alarm_label'] == alarm_label:
            alarm_list_sched.remove(alarms)
            #Removing entry from alarm_list_sched when alarm trigger
    log_info = "Alarm Triggered : " + str(briefing)
    logging.info(log_info) #Logging that the alarm has triggered

if __name__ == "__main__":
    announcement()
    top_news_titles()
    uk_covid_announcement()
    current_weather()
