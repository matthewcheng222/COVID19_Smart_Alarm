import os
import json
import logging
import datetime
from datetime import datetime
from time import strptime
from uk_covid19 import Cov19API

with open(os.path.dirname(__file__) + "/../../config.json") as config_file:
    config = json.load(config_file)

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
    try: #Fetching UK COVID-19 data if no error is returned
        last_updated = data["lastUpdate"][:10]
        last_updated = datetime.strptime(last_updated, "%Y-%m-%d")
        last_updated = datetime.strftime(last_updated, "%A, %d %B, %Y")
        main = data["data"]
        new_day_cases = main[0]['cases']['daily']
        new_cum_cases = main[0]['cases']['cumulative']
        new_day_death = main[0]['deaths']['daily']
        new_cum_death = main[0]['deaths']['cumulative']
        if new_day_death is None: #Changing None -> 0
            new_day_death_new = 0
        if new_cum_death is None: #Changing None -> 0
            new_cum_death_new = 0
        output = "For COVID-19, as of " + str(last_updated) + ", there are "\
            + str(new_day_cases) + " new cases and "\
                + str(new_day_death_new) + " new death cases at " + area\
                    + ". There are " + str(new_cum_cases) + " cases and "\
                        + str(new_cum_death_new)\
                            + " death cases cumulatively. "
        covid_announcement_log = "COVID-19 announcement returned : "\
            + str(output)
        logging.info(covid_announcement_log)
        #Logging created COVID-19 notification
        return output
    except IsADirectoryError: #Error returned by the API
        logging.error("Error : The filename is not defined in the path")
    except ValueError: #Error returned by the API
        error = "Error : The filename does not end with the correct"\
            + "extension for the requested format"
        logging.error(error)
