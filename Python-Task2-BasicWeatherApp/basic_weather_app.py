import requests

print("=== Basic Weather App ===")

API_KEY = "YOUR_API_KEY_HERE"

location = input(
    "Enter city name or ZIP code (example: Trichy or 620001,IN): "
).strip()

if not location:
    
    print("Please enter a city name or ZIP code.")

elif API_KEY == "YOUR_API_KEY_HERE":
    print("Please add your OpenWeatherMap API key in the code.")

else:
    url = "https://api.openweathermap.org/data/2.5/weather"

    parameters = {
        "q": location,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=parameters, timeout=10)

        if response.status_code == 200:
            data = response.json()

            city = data["name"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            description = data["weather"][0]["description"]

            print("\n===== CURRENT WEATHER =====")
            print("Location:", city)
            print("Temperature:", temperature, "°C")
            print("Humidity:", humidity, "%")
            print("Weather condition:", description)
            print("===========================")

        elif response.status_code == 404:
            print("Location not found. Please check your city or ZIP code.")

        elif response.status_code == 401:
            print("Invalid API key. Please check your API key.")

        else:
            print("Unable to get weather information.")
            print("Error code:", response.status_code)

    except requests.exceptions.RequestException:
        print("Network error. Please check your internet connection.")
        