import os
import json
import logging
import sched
import time
from newsapi import NewsApiClient
from flask import Markup

with open(os.path.dirname(__file__) + "/../../config.json") as config_file:
    config = json.load(config_file)

s = sched.scheduler(time.time, time.sleep)

notifications_list = []
dismissed_notifications = []

def top_news_details() -> dict:
    """
    Appending titles and details of top news stories to notifications_list:

    This function will take titles and description of top news stories and
    adding them to notifications_list in the format of a dictionary

    The dictionary take the format of : {'title':title, 'content':content}
    User-defined variables include:
        - Number of news stories to return
    """
    language = config["news"]["language"]
    newsapi = NewsApiClient (api_key = config["news"]["api_key"])
    top_headlines = newsapi.get_top_headlines (language = language)
    refresh_freq = config["news"]["news_refresh_frequency"]
    if top_headlines["status"] == "ok": #Fetching news if API status is OK
        articles = top_headlines["articles"]
        results = []
        to_export = config["news"]["no_of_news"]
        #User defined no. of news to export
        for entry in articles[0:to_export]:
            details = {key: entry[key] for key in entry.keys()\
                & {'title', 'description', 'url'}}
            results.append(details)
        for details in results:
            title = details['title']
            url = details['url']
            url_link = "(Click " + Markup("<a href='%s'>Here</a>") % (url)\
                + " to learn more.)"
            content = Markup("%s <br> %s")%(details['description'], url_link)
            dictionary = {'title' : title, 'content' : content}
            if dictionary not in dismissed_notifications:
                if dictionary not in notifications_list:
                    notifications_list.append(dictionary)
                    news_n_log = "News notification created : "\
                        + str(dictionary)
                    logging.info(news_n_log)
                    #Logging created news notification
    elif top_headlines["status"] == "error": #API status is error -> log
        error_output = "Error : " + top_headlines["code"] + " - "\
            + top_headlines["message"]
        logging.error(error_output) #Logging message of error
    s.enter(refresh_freq, 1, top_news_details, ) #Rate of fetching data