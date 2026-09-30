import tkinter as tk
import requests

API_KEY = "YOUR_API_KEY"


def get_weather():
    city = city_entry.get()

    url = "https://api.openweathermap.org/data/2.5/forecast"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code != 200:
        result_label.config(text="City not found!")
        return

    # Temperature
    temperature = data["list"][0]["main"]["temp"]

    # Chance of rain
    rain_chance = data["list"][0]["pop"] * 100

    result_label.config(
        text=f"Temperature: {temperature}°C\n"
             f"Chance of Rain: {rain_chance:.0f}%"
    )


# Create window
window = tk.Tk()
window.title("Weather Reporter")
window.geometry("400x300")


# Heading
heading = tk.Label(
    window,
    text="Weather Reporter",
    font=("Arial", 22, "bold")
)
heading.pack(pady=20)


# City label
city_label = tk.Label(
    window,
    text="Enter City:"
)
city_label.pack()


# City input
city_entry = tk.Entry(
    window,
    width=25,
    font=("Arial", 14)
)
city_entry.pack(pady=10)


# Button
weather_button = tk.Button(
    window,
    text="Get Weather",
    command=get_weather
)
weather_button.pack(pady=10)


# Result
result_label = tk.Label(
    window,
    text="Temperature: --\nChance of Rain: --",
    font=("Arial", 16)
)
result_label.pack(pady=20)


# Start application
window.mainloop()
