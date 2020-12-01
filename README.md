# COVID19_Smart_Alarm

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

## Built With

* [Python3](https://www.python.org/) - The Programming Language Used
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - The WSGI Web Application Framework used
* [PyTTSx3](https://github.com/nateshmbhat/pyttsx3) - Used for converting Text-to-Speech 

## Authors

* **Matthew Cheng** - *Initial work* - [matthewcheng222](https://github.com/matthewcheng222)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


