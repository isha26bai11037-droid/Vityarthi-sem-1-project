## Problem Statement
People often need quick and simple weather information before travelling, going to college, or planning outdoor activities. However, weather applications can provide a large amount of information that may not be necessary for a basic weather check.
The Automated Weather Reporter aims to solve this problem by providing a simple Python-based application where the user enters a city name and receives two important weather details:
Current temperature in Celsius
Chance of rain in percentage
The application retrieves the information automatically using the OpenWeatherMap API and displays it through a simple graphical interface.
## Scope of the Project
The scope of this project is to develop a beginner-friendly desktop weather application using Python.
Included in the project:
Accepting a city name from the user
Connecting to the OpenWeatherMap API
Retrieving weather forecast data
Extracting temperature information
Extracting precipitation probability
Converting rain probability into a percentage
Displaying the results using a Tkinter GUI
Basic handling of invalid city/API responses
Not included in the current version:
User accounts or login
Database storage
Weather history
Automatic location detection
Detailed multi-day weather dashboard
Weather notifications
Mobile application
These features can be added in future versions.
## Target Users
The application is designed for:
Students who want to check the weather quickly.
Beginners learning Python who want to understand APIs and GUI programming.
General users who need basic weather information.
People planning simple outdoor activities who want to check temperature and rain probability.
The interface is intentionally kept simple so that users do not need technical knowledge to operate it.
## High-Level Features
1. City Search
The user can enter the name of a city into the application.
2. Live Weather Data
The application retrieves weather information from the OpenWeatherMap API.
3. Temperature Display
The current temperature is displayed in degrees Celsius (°C).
4. Chance of Rain
The application displays the probability of precipitation as a percentage (%).
5. Simple Graphical Interface
The application uses Tkinter to provide a simple interface containing:
City input box
Get Weather button
Weather result area
6. Basic Error Handling
If the city cannot be found or the API request is unsuccessful, the application displays an appropriate error message instead of showing incorrect weather information.
7. Beginner-Friendly Design
The project uses a small number of Python concepts and is designed to be easy to understand, modify, and extend.
