Basic Weather App

Project Description

The Basic Weather App is a Python-based application that retrieves current weather information for a user-specified city using the OpenWeatherMap API. It displays the temperature, humidity, and weather conditions.

Features

- Accepts a city name or ZIP code as input.
- Fetches live weather information using the OpenWeatherMap API.
- Displays the city name.
- Displays temperature in Celsius.
- Displays humidity percentage.
- Shows the current weather description.
- Handles invalid city names.
- Handles API errors and internet connection issues.

Technologies Used

- Python 3
- Requests library
- OpenWeatherMap API

Installation

Install the required Requests library using:

pip install requests

How to Run

1. Install Python 3.
2. Install the Requests library.
3. Create an account on OpenWeatherMap.
4. Generate an API key.
5. Add your API key securely to the program.
6. Run the following command:

python basic_weather_app.py

Sample Input

Enter city name or ZIP code: Trichy

Sample Output

===== CURRENT WEATHER =====
Location: Tiruchirappalli
Temperature: 30°C
Humidity: 65%
Weather condition: scattered clouds
===========================

Note: The above output is only an example. Actual weather information changes depending on the location and current weather conditions.

Learning Outcomes

- Learned how to use a third-party API.
- Practiced Python requests and JSON handling.
- Understood exception handling.
- Learned to retrieve and display live weather information.

Author

Jayasri S.

Internship

Oasis Infobyte – Python Programming Internship

API Reference

https://openweathermap.org/api