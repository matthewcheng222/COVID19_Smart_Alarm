# COVID19_Smart_Alarm

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![Documentation Status](https://readthedocs.org/projects/ansicolortags/badge/?version=latest)](http://ansicolortags.readthedocs.io/?badge=latest) [![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/matthewcheng222/COVID19_Smart_Alarm/blob/main/LICENSE)

COVID19_Smart_Alarm is developed for Continous Assessment 3 of the ECM1400 module. It is an alarm clock with smart features, which is espically useful during the global pandemic. 

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

After cloning, open ```config.json``` and fill in the following feilds. 


For the first section "current_weather", replace the contents represented with <feild> below: 
    
1. ```"api_key":"<feild>"``` - Your own API key from openweather. (Can be obtained [here](https://openweathermap.org/appid)) 
   
2. ```"lat":"<feild>"``````"lon":"<feild>"``` - Your location in terms of latitude and longitude (Can be obtained [here](https://www.latlong.net/))
   
3. ```"units":"<feild>"``` - Your preference of units to be displayed. Below are units that you can choose from:

       *standard (temperature in Kelvin, wind speed in meter/sec)*
       
       *metric (temperature in Celsius, wind speed in meter/sec)*
       
       *imperial (temperature in Fahrenheit, wind speed in miles/hour)*
       
4. ```"wx_refresh_frequency":<feild>``` - How often would you like weather data to refresh (in seconds)
   
5. ```"wind_speed_trigger":<feild``` - If real-time wind speed exceeds this value, notifications will trigger (in units of your selection)
    
    
For the second section "news", fill in the following feilds:

6. ```"api_key":"<feild>"``` - Your own API key from newsapi. (Can be obtained [here](https://newsapi.org/))
    
7. ```"language":"<feild>"``` - The language of news. (The 2-letter ISO-639-1 code)
    
8. ```"no_of_news":<feild>``` - The number of news stories to return (announcements and notifications)
    
9. ```"news_refresh_frequency":<feild>``` - How often would you like news data to refresh (in seconds)


For the third section "covid19_api", fill in the following feilds:

10. ```"area_name":<feild>``` - The location/region that you are in

11. ```"covid_refresh_frequency":<feild>``` - How often would you like COVID-19 data to be updated

12. ```"no_to_trigger_threshold":<feild>``` - Number of daily cases above this value will trigger a COVID-19 notification

For the last section "pyttsx3", fill in the following feilds:

13. ```"speak_rate":<feild>``` - The rate of speaking for pyttsx3

*Note : API keys may require serval hours to be activated*

***

Other than config.json, the favicon of the webpage and the logo of the webpage can also be replaced. 

#### Replacing the Favicon

If you have a favicon with type .ico and resolution 16x16 px. You can replace the favicon of the website by putting ```favicon.ico``` into ```CA3 - COVID19 Smart Alarm/static```

#### Replacing the Logo

The logo can be replaced with a .jpg file which is square in dimension, by putting ```image.jpg``` into ```CA3 - COVID19 Smart Alarm/static/images```

*Note : If the file name of favicon and logo replaced is not ```favicon.ico``` and ```image.jpg``` respectively, you will need to edit the name of file in the index function, replacing favicon.ico in ```favicon = "/static/favicon.ico"``` to be the name of your file, and replacing image.jpg in ```image = "image.jpg"``` to be the name of your file. 

***

### Running the program

Open the file master.py to run the program. You could either use your terminal/command prompt or use an IDE.


If you are using a terminal:

a. Open your termial 

b. Change directory to the folder ```CA3 - COVID19 Smart Alarm``` of this project using ```cd <folder path>```, where <folder path> is the path on your machine. 
    
c. Using the command ```python3 master.py```, the program will start running.


If you are using an IDE:

a. Open master.py on your IDE

b. Run the program (Varies between IDE's)

***

After running master.py using the methods above, you will see the ```Serving Flask app "master" (lazy loading)``` on your terminal.

Visit ```127.0.0.1:5000``` or ```127.0.0.1:5000/index``` using a browser. You should see the embedded HTML template with widgets of notification on the right hand side and a section called 'Alarm' on the left. The title "ECM1400CA3 COVID-19 Smart Alarm" will appear on the middle and a form can be found below the title. 

If you can access and see the page correctly, the setup for this project is complete. 

***

## Features

### Creating Alarms

An alarm could be created using the form in the middle of the page, below are some instructions on how to do it.

Fill in the ```date/time``` feild with the date and time you would like the alarm to trigger (In the format of YYYY-MM-DD HH:MM)

Fill in the ```Update label``` feild for the label of the alarm

Tick the ```Include news briefing?``` feild if you would like news briefing to be included in your alarm announcement

Tick the ```Include weather briefing?``` feild if you would like weather briefing to be included in your alarm announcement

FInally, click the ```Submit``` button to create the alarm

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

1. Wind Speed notification

Wind speed notification will contain the wind speed and direction if the wind speed is higher than the trigger threshold (set by user in config.json)

2. Rain Probability notification 

Rain probability notification will contain the probability of rain of the day

3. Daily Temp UVI notification 

Daily Temp UVI notification will contain the maximum and minimum temperature of the day, as well as the UV index in midday. 

#### UK COVID-19 Notifications

The part of UK COVID-19 notifications is divided into 2 parts, ```national cases notification``` and ```covid infection threshold notification```, where covid infection threshold notification is triggered by daily new case is higher than the trigger threshold (set by user in config.json)

1. National Case notification 

National case notification contains the latest national COVID cases and the release date of data. A new notification will be created when new data has been released for the day. 

2. COVID-19 Infection Threshold notification 

COVID-19 infection threshold notification contains the threshold that new and cumulative cases have reached.

#### Top News Notifications 

The part of top news notification creates notifications according to the preselect number of news to include (set by user in config.json). Where the title of the notification widget is the title of the news, and the contents of the widget is the description of the news. News data are refreshed according to the frequency set in config.json. 

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
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - The WSGI Web Application Framework used
* [PyTTSx3](https://github.com/nateshmbhat/pyttsx3) - Used for converting Text-to-Speech 

## Versioning

[SemVer](http://semver.org/) is used for versioning

## Authors

* **Matthew Cheng** - *Initial work* - [matthewcheng222](https://github.com/matthewcheng222)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
