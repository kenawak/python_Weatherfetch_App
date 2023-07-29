import datetime as dt
import requests
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('API_KEY', 'r').read()

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

def get_weather():
    try:
        city = city_entry.get()
        url = BASE_URL + "appid=" + API_KEY + "&q=" + city
        response = requests.get(url).json()

        temp_kelvin = response['main']['temp']
        temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
        feels_like_kelvin = response['main']['feels_like']
        feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
        humidity = response['main']['humidity']
        wind_speed = response['wind']['speed']
        description = response['weather'][0]['description']
        sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
        sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

        result_label.config(text=f"Temperature in {city}: {temp_celsius:.2f}°C or {temp_fahrenheit:.2f}°F\n"
                                 f"Temperature in {city} feels like: {feels_like_celsius:.2f}°C or {feels_like_fahrenheit:.2f}°F\n"
                                 f"Humidity in {city}: {humidity}%\n"
                                 f"Wind Speed in {city}: {wind_speed}m/s\n"
                                 f"Sun rises in {city} at  {sunrise_time} local time.\n"
                                 f"Sun sets in {city} at  {sunset_time} local time.\n"
                                 f"General Weather in {city}: {description}")
    except:
        result_label.config(text="Enter a city!")


# Create the tkinter GUI window
root = tk.Tk()
root.title("Weather App")

# Set the theme for the GUI
style = ThemedStyle(root)
style.set_theme("arc")  # Choose a theme you like (e.g., "scidblue", "radiance", "adapta", etc.)

# City input
city_name = ttk.Label(root, text="Enter your city")
city_name.pack(padx=10, pady=10)

city_entry = ttk.Entry(root, font=("Helvetica", 16))
city_entry.pack(pady=10)

# Fetch weather button
fetch_button = ttk.Button(root, text="Fetch Weather", command=get_weather)
fetch_button.pack()

# Weather result display
result_label = ttk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=20)

root.mainloop()
