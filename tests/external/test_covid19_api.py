import os
import json
from json import dumps
from requests import get
from uk_covid19 import Cov19API
from uk_covid19.exceptions import FailedRequestError
import requests

with open(os.path.dirname(__file__) + "/../../config.json") as config_file:
    config = json.load(config_file)

endpoint = "https://api.coronavirus.data.gov.uk/v1/data"
test_filters = [
    'areaType=nation',
    'areaName=england'
]
test_structure = {
    "name": "areaName",
    "date": "date",
    "newCases": "newCasesByPublishDate"
}
api_params = {
    "filters":str.join(";", test_filters),
    "structure":dumps(test_structure, separators=(",", ":")),
    "latestBy":"cumCasesByPublishDate"
}

def test_covid_api_endpoint():
    data = Cov19API.options()
    server_url = data['servers'][0]['url']
    assert Cov19API.endpoint == server_url

def test_covid_api_response():
    response = requests.get(endpoint)
    assert response.status_code == 200

def test_covid_api_results():
    response = get(endpoint, params=api_params, timeout = 10)
    results = response.content.decode()
    data = json.loads(results)
    assert data['length'] >= 1

def test_covid_api_type():
    response = get(endpoint, params=api_params, timeout = 10)
    results = response.content.decode()
    data = json.loads(results)
    assert isinstance(data, dict)

def test_news_api_locationerror():
    test_filters = [
    'areaType=nation',
    'areaName=france'
    ]
    test_structure = {
        "name": "areaName",
        "date": "date",
        "newCases": "newCasesByPublishDate"
    }
    api_params = {
        "filters":str.join(";", test_filters),
        "structure":dumps(test_structure, separators=(",", ":")),
        "latestBy":"cumCasesByPublishDate"
    }
    response = get(endpoint, params=api_params, timeout = 10)
    assert response.status_code == 204 
    #The request was successfully processed, but there were no records matching the requested criteria.
