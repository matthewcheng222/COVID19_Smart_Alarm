import os
import json
from newsapi import NewsApiClient
import requests

with open(os.path.dirname(__file__) + "/../../config.json") as config_file:
    config = json.load(config_file)

api = config["news"]["api_key"]
language = config["news"]["language"]
newsapi = NewsApiClient (api_key = api)
top_headlines = newsapi.get_top_headlines (language = language)

def test_news_api_status() -> None:
    assert top_headlines['status'] == "ok"

def test_news_api_results() -> None:
    assert top_headlines['totalResults'] >= 1

def test_news_api_type() -> None:
    assert isinstance(top_headlines, dict)

def test_news_api_noapikey() -> None:
    api = ""
    newsapi = "https://newsapi.org/v2/everything?apiKey=%s&language=%s" % (api, language)
    response = requests.get(newsapi)
    assert response.status_code == 401

def test_news_api_languageerror() -> None:
    language = "uk"
    newsapi = "https://newsapi.org/v2/everything?apiKey=%s&language=%s" % (api, language)
    response = requests.get(newsapi)
    assert response.status_code == 400
