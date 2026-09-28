## Automated Weather Reporter
A beginner friendly Python application that displays the current temperature and chance of rain for a city using the OpenWeatherMap API.
## Features
Enter any city name
Get the temperature in Celsius
Get the chance of rain as a percentage
Uses live weather data from Openweathermap
## Requirements
Before running the project, make sure you have:
Python3 installed on the laptop
An Openweathermap account
An Openweathermap API key
## install the requests library
open terminal inside the project folder
**pip install requests**
## get an openweathermap api key
go to open weather map
create account and login to it 
create your api keys and then copy them 
 
## CODE EXPLANATION 
step1: importing libraries 
**import tkinter as tk**
**import requests**

{tkinter is used to create graphical user inetrface
requests is used to send request to thr open weather map api}

step2: Adding your api key
**API_KEY = "YOUR_API_KEY"**
{The api key allows the program to access weather information from Openweathermap}

step3: creating the weather function
**def get_weather():**
{this function runs when the user clicks the get weather button}
the user enters the city name 
**city = city_entry.get()**

step4: creating the api URL
this is the openweathermap api endpoint used to obtain forecast information

step5: Sending the request
**parameters can be called by params**

These parameters tell the api that
q = which city we want
appid = our api key
units = in celsius 

The request is then sent
**response = requests.get(url, params=params)**


step6: checking for errors
**if response.status_code != 200:**
    **result_label.config(text="City not found!")**
    **return**

The program checks if the api request is successful
A status code of 200 means the request is successful.
If the city spelling is wrong, the program displays an error message instead of continuing.

step7: converting the user response to python data
**data = response.json()**
the api sends the weather information in JSON format

response.json() converts that information into python data that we can access.

step8: Getting the temperature
**temperature = data["list"][0]["main"]["temp"]**
this accesses the temperature from the weather data.
For example, if the api provides:30.5
the program stores
temperature = 30.5

step9: displaying the result
Temperature: 30°C
Chance of Rain: 60%

## Running the Application
in the project directory, run
**python weather_app.py**
A window called Weather Reporter will open

## City not found
check that the city name is spelled correctly.

Make sure:
the api key was copied correctly.



