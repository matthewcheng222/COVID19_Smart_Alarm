import os
import json
import logging
from newsapi import NewsApiClient

with open(os.path.dirname(__file__) + "/../../config.json") as config_file:
    config = json.load(config_file)
    
def top_news_titles() -> str:
    """
    Returning titles of top news stories (for announcement):

    User-defined variables include:
        - Number of news stories to return
    """
    api = config["news"]["api_key"] #API key of user
    language = config["news"]["language"] #Language of news to be fetched
    newsapi = NewsApiClient (api_key = api)
    top_headlines = newsapi.get_top_headlines (language = language)
    if top_headlines["status"] == "ok": #Fetching news if API status is OK
        articles = top_headlines["articles"]
        results = []
        to_export = config["news"]["no_of_news"]
        #User defined no. of news to export
        for sources in articles:
            results.append(sources["title"])
        news_list = results[0:to_export]
        news_join = ", "
        news_join = news_join.join(news_list)
        output = "Here are the top " + str(to_export)\
            + " news story titles for today: " + news_join
        news_a_log = "News announcement created : " + str(output)
        logging.info(news_a_log) #Logging created news announcement
    elif top_headlines["status"] == "error": #API status is error -> log
        error_output = "Error : " + top_headlines["code"] + " - "\
            + top_headlines["message"]
        logging.error(error_output)
    return output