# COVID19_Smart_Alarm

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![Documentation Status](https://readthedocs.org/projects/ansicolortags/badge/?version=latest)](http://ansicolortags.readthedocs.io/?badge=latest) [![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/matthewcheng222/COVID19_Smart_Alarm/blob/main/LICENSE) [![PyPI status](https://img.shields.io/pypi/status/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)

COVID19_Smart_Alarm is developed for Continous Assessment 3 of the ECM1400 module. It is an Alarm Clock with smart features, which is espically useful during the times of a global pandemic. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

The smart alarm is written in Python 3 programming language. In order to run the program, you will need a working Python 3 interpreter (Available [here](https://www.python.org/downloads/)). You will also need a text-editor or an Integrated development environment (IDE) if you wish to develop further on this project.

*Note: Due to the format of assessment submission, a virtual environment is **not** used when developing.*

### Installing

Depending on your programming environment, new Python Packages may need to be installed for the program to work. Information of how to do this can be found below.

*Note: If you are developing this program on UNIX systems, Both Python 2 and Python 3 may be installed. If this is the case, use **python3** instead of **python** and use **pip3** instead of **pip***

Check if you have the latest version of Python in the command prompt/ terminal:

```
python --version
```

If you have a Python version below 3.7 or if you see "python: command not found". Please download and install a new Python interpreter [here](https://www.python.org/downloads/).

***

Install Python packages that are required for this project, including:

1. Flask
    ```
    pip install Flask
    ```
2. uk_covid_19
    ```
    pip install uk-covid19
    ```
3. newsapi
    ```
    pip install newsapi-python
    ```
4. pyttsx3
    ```
    pip install pyttsx3
    ```
5. requests
    ```
    pip install requests
    ```

***

Clone this repository on your local computer using [this link](https://github.com/matthewcheng222/COVID19_Smart_Alarm.git) or by any other means.

### Configuration

After cloning, open ```config.json``` and fill in the following feilds. 

*Note : Some feilds come with a default value, the end of this section shows the list and meaning of the default values*

For **Section 1 - "Current_Weather"**, replace the contents represented with <feild>: 
    
* ```"api_key":"<feild>"``` - Your own API key from openweather. (Can be obtained [here](https://openweathermap.org/appid)) 
   
* ```"lat":"<feild>"``` and ```"lon":"<feild>"``` - Your location in terms of latitude and longitude (Can be obtained [here](https://www.latlong.net/))
   
* ```"units":"<feild>"``` - Your preference of units to be displayed. Below are units that you can choose from:

    * ```standard``` (temperature in Kelvin, wind speed in meter/sec)
       
    * ```metric``` (temperature in Celsius, wind speed in meter/sec)
       
    * ```imperial``` (temperature in Fahrenheit, wind speed in miles/hour)
       
* ```"wx_refresh_frequency":<feild>``` - How often would you like weather data to refresh (in seconds)
   
* ```"wind_speed_trigger":<feild``` - If real-time wind speed exceeds this value, notifications will trigger (in units of your selection)
    
    
For **Section 2 - "News"**, replace the contents represented with <feild>:

* ```"api_key":"<feild>"``` - Your own API key from newsapi. (Can be obtained [here](https://newsapi.org/))
    
* ```"language":"<feild>"``` - The language of news. (The 2-letter ISO-639-1 code)
    
* ```"no_of_news":<feild>``` - The number of news stories to return (announcements and notifications)
    
* ```"news_refresh_frequency":<feild>``` - How often would you like news data to refresh (in seconds)


For **Section 3 - "COVID19_API"**, replace the contents represented with <feild>:

* ```"area_name":<feild>``` - The location/region that you are in

* ```"covid_refresh_frequency":<feild>``` - How often would you like COVID-19 data to be updated

* ```"no_to_trigger_threshold":<feild>``` - Number of daily cases above this value will trigger a COVID-19 notification

For **Section 4 - "PYTTSX3"**, replace the contents represented with <feild>:

* ```"speak_rate":<feild>``` - The rate of speaking for pyttsx3

*Note : API keys may require serval hours to be activated*

#### Default Values of config.json

Below are the list and meanings of default values which is included in config.json and replacing them is not necessary

#### "Current Weather"

* ```"lat":"50.716667"``` and ```"lon":"-3.533333"``` -> Coordinates of Exeter

* ```"units":"metric"``` -> Default units are set to metric (temperature in Celsius, wind speed in meter/sec)

* ```"wx_refresh_frequency":3600``` -> Weather information will be updated every hour (3600 seconds) by default

* ```"wind_speed_trigger":10.7``` -> Wind notification will be triggered when wind speed reaches 10.7 m/s (Strong Breeze in the Beaufort scale)

#### "News"

* ```"language":"en"``` -> Default language of news returned are set to English 

* ```"no_of_news":5``` -> Default number of news to show in notifications list is 5

* ```"news_refresh_frequency":3600``` -> News data will be updated every hour by default

#### "COVID19_API"

* ```"area_name":"Exeter"``` -> Default location of local COVID-19 cases is Exeter

* ```"covid_refresh_frequency":3600``` -> COVID-19 datawill be refreshed every hour by default 

* ```"no_to_trigger_threshold":10000``` -> COVID-19 threshold reached notification will trigger if daily COVID-19 cases is above 10000 by default 

#### "PYTTSX3"

* ```"speak_rate":165``` -> The speech rate of pyttsx3 engine is set to 165 by default

***

Other than config.json, the favicon of the webpage and the logo of the webpage can also be replaced. Instructions are listed below. 

#### Replacing the Favicon

* If you have a favicon with type .ico and resolution 16x16 px. You can replace the favicon of the website by putting ```favicon.ico``` into ```CA3 - COVID19 Smart Alarm/static```

#### Replacing the Logo

* The logo can be replaced with a .jpg file which is square in dimension, by putting ```image.jpg``` into ```CA3 - COVID19 Smart Alarm/static/images```

*Note : If the file name of favicon and logo replaced is not ```favicon.ico``` and ```image.jpg``` respectively, you will need to edit the name of file in the index function, replacing favicon.ico in ```favicon = "/static/favicon.ico"``` to be the name of your file, and replacing image.jpg in ```image = "image.jpg"``` to be the name of your file. 

***

### Running the program

Open the file master.py to run the program. You could either use your terminal/command prompt or use an IDE.


If you are using a terminal:

1. Open your termial 

2. Change directory to the folder ```CA3 - COVID19 Smart Alarm``` of this project using ```cd <folder path>```, where <folder path> is the path on your machine. 
    
3. Using the command ```python3 master.py```, the program will start running.


If you are using an IDE:

1. Open master.py on your IDE

2. Run the program (Varies between IDE's)

***

After running master.py using the methods above, you will see the ```Serving Flask app "master" (lazy loading)``` on your terminal.

Visit ```127.0.0.1:5000``` or ```127.0.0.1:5000/index``` using a browser. You should see the embedded HTML template with widgets of notification on the right hand side and a section called 'Alarm' on the left. The title "ECM1400CA3 COVID-19 Smart Alarm" will appear on the middle and a form can be found below the title. 

If you can access and see the page correctly, the setup for this project is complete. 

***

## Features

### Creating Alarms

An alarm could be created using the form in the middle of the page, below are some instructions on how to do it.

1. Fill in the ```date/time``` feild with the date and time you would like the alarm to trigger (In the format of YYYY-MM-DD HH:MM)

2. Fill in the ```Update label``` feild for the label of the alarm

3. Tick the ```Include news briefing?``` feild if you would like news briefing to be included in your alarm announcement

4. Tick the ```Include weather briefing?``` feild if you would like weather briefing to be included in your alarm announcement

5. FInally, click the ```Submit``` button to create the alarm

*Note : Browsers which do not support datetime_local feild do not have a date/time picker, therefore may require manual entry of dates and time*

***

### Removing/Dismissing Alarms and Notifications

An alarm/notification can be removed/dismissed using the 'x' on the top right hand side of the widget. 

*Note : the alarm/notification is dismissed by removing it from alarms/notifications_list, and will then be added to the list dismissed_alarms/notifications*

***

### Ringing of an alarm

When an alarm triggers (i.e time of alarm is now), an announcement will be played, contents of the announcement depends on what have been selected when creating the alarm. By default (nothing was ticked when creating an alarm), an announcement contains time briefing, weather briefing, covid briefing and news briefing. 

*Note : Time announcement and COVID-19 briefing are always announced*

***

### Notifications

The notifications column (on the right hand side) is automatically updated by functions and require no user input at run time. However, the update frequency of those notifications may be tweaked in the config.json file. 

The features of each notification are as follows:

#### Weather Notifications

The part of weather notifications is divided into 3 parts, namely ```wind speed notification```, ```rain probability notification``` and ```daily temp uvi notification```. Other than wind speed notification, all notifications are triggered when the program runs. 

* Wind Speed notification

    * Wind speed notification will contain the wind speed and direction if the wind speed is higher than the trigger threshold (set by user in config.json)

* Rain Probability notification 

    * Rain probability notification will contain the probability of rain of the day

* Daily Temp UVI notification 

    * Daily Temp UVI notification will contain the maximum and minimum temperature of the day, as well as the UV index in midday. 

#### UK COVID-19 Notifications

The part of UK COVID-19 notifications is divided into 2 parts, ```national cases notification``` and ```covid infection threshold notification```, where covid infection threshold notification is triggered by daily new case is higher than the trigger threshold (set by user in config.json)

* National Case notification 

    * National case notification contains the latest national COVID cases and the release date of data. A new notification will be created when new data has been released for the day. 

* COVID-19 Infection Threshold notification 

    * COVID-19 infection threshold notification contains the threshold that new and cumulative cases have reached.

#### Top News Notifications 

The part of top news notification creates notifications according to the preselect number of news to include (set by user in config.json). Where the title of the notification widget is the title of the news, and the contents of the widget is the description of the news. News data are refreshed according to the frequency set in config.json. 

***

## Testing

A number of tests files have been created and included with this project, and they can be distributed into 2 categories:

### Tests for External Services

Tests for External Services are tests designed to test the APIs functionality, and whether they are returning expected response code and data types.

* ```test_covid19_api.py``` includes 5 test cases for the COVID-19 API, provided by Public Health England. The breakdown of the test can be found below

    * ```test_covid_api_endpoint``` tests whether the API endpoint is correct, therefore ensures data being fetched from the correct source
    
    * ```test_covid_api_response``` tests whether the API returns response code 200 (Normal)
    
    * ```test_covid_api_results``` tests whether the API returns more than 1 COVID-19 results
    
    * ```test_covid_api_type``` tests whether the API returns the correct data type (dictionary)
    
    * ```test_news_api_locationerror``` tests whether the API returns response code 204 due to location error (France not supported by this API)
    
* ```test_news_api.py``` includes 5 test cases designed for the newsapi. The breakdown of the test can be found below 

    * ```test_news_api_status``` tests whether the API returns status ```ok``` when called
    
    * ```test_news_api_results``` tests whether the API returns more than 1 results
    
    * ```test_news_api_type``` tests whether the API returns the correct data type (dictionary)
    
    * ```test_news_api_noapikey``` tests whether the API returns status code 401 (Unauthorized) if there is no API key
    
    * ```test_news_api_languageerror``` tests whether the API returns code 400 (Bad Request) if language requested is invalid
    
* ```test_weather_api.py``` includes 5 tests cases for the openweatherapi. The breakdown of the test can be found below

    * ```test_weather_api_status``` tests whether the API returns response code 200 (Normal)
    
    * ```test_weather_api_type``` tests whether the API returns the correct data type (dictionary)
    
    * ```test_weather_api_noapikey``` tests whether the API returns code 401 (Unauthorized) if API key is missing 
    
    * ```test_weather_api_locationerror``` tests whether the API returns code 400 (Bad Request) if invalid latitude and longitude is inputted
    
    * ```test_weather_api_invalidunit``` tests whether the API returns code 200 (Normal) even if an invalid unit is inputted (default unit for API is set to standard)
    
### Unit Testing 

***

## Known Issues

### Alarms do not trigger on the exact 'moment'

Since this project uses Flask as a web application freamework, the webpage refreshes every minute after the last event has been done (e.g creating an alarm, removing an alarm). The alarm only triggers/rings when the webpage refreshes, therefore the alarm may not ring at the exact moment, but runs in same minute when the webpage refreshes. 

### UK COVID-19 data

Since UK COVID-19 data is updated once every day by Public Health England, COVID-19 data may not be from the same date when the program runs. To reduce confusion, I have included the last updated time of these data.

Moreover, since the death data (daily and cumulative) are not updated everyday, but once every couple of days. New and cumulative death cases in announcements may be incorrect. 

***

## Built With

* [Python3](https://www.python.org/) - The Programming Language Used
* [Requests](https://pypi.org/project/requests/) - Used to get data for various APIs
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - The WSGI Web Application Framework used
* [PyTTSx3](https://github.com/nateshmbhat/pyttsx3) - Used for converting Text-to-Speech 
* [NewsAPI](https://newsapi.org) - Used for fetching up-to-date news articles
* [OpenweatherAPI](https://openweathermap.org/api) - Used for fetching real-time weather data
* [PHE COVID19 Dashboard API](https://github.com/publichealthengland/coronavirus-dashboard-api-python-sdk) - Used for fetching official COVID-19 figures in the UK

## Versioning

[SemVer](http://semver.org/) is used for versioning

## Authors

* **Matthew Cheng** - *Initial work* - [matthewcheng222](https://github.com/matthewcheng222)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
