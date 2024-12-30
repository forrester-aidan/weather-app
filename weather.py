import requests
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry('400x300')
root.title("Weather App")

city_label = tk.Label(root, text="City:")
city_label.pack()
city_entry = tk.Entry(root)
city_entry.pack()

fetch_button = tk.Button(root, text="Fetch Weather")
fetch_button.pack()

weather_label = tk.Label(root, text="")
weather_label.pack()

# Define the function to fetch weather data
def fetch_weather():
    city = city_entry.get()
    api_key = "05a5f4a80dba055badc6bf9a980df7ba"
    url = "http://api.weatherstack.com/current"

    params = {
        'access_key': api_key,  # Replace with your Weatherstack API key
        'query': city,
    }
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        temperature = data['current']['temperature']
        weather = data['current']['weather_descriptions'][0]
        weather_label.config(text=f"Temperature: {temperature}°C\nWeather: {weather}")
    except Exception as e:
        messagebox.showerror("Error", "Unable to fetch weather data")

fetch_button.config(command=fetch_weather)

# Start the GUI main loop
root.mainloop()