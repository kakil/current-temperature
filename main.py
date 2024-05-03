from dotenv import load_dotenv
import os
import requests
import json
import tkinter as tk
from tkinter import ttk


load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")

# How to make a call using open weather map api
# http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={API key}
#
# API Call for city name:
# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

# Global variable to store the result label widget
result_label = None


def gui():
    global result_label
    root = tk.Tk()
    root.title("City Temperature")
    frame = ttk.Frame(root, padding=10)
    frame.grid()
    ttk.Label(frame, text="Enter City: ").grid(column=0, row=0)

    city_entry = ttk.Entry(frame, width=20)
    city_entry.grid(column=1, row=0)

    result_label = ttk.Label(frame, text="Temperature will be displayed here")
    result_label.grid(column=0, row=3, columnspan=2)

    submit_button = ttk.Button(frame, text="Submit", command=lambda: get_temperature(city_entry.get()))
    submit_button.grid(column=1, row=1)

    root.mainloop()


def get_temperature(city):

    try:
        request = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")

        if request.status_code == 200:
            json_data = request.json()
            # print(json_data)

            # Get temp value
            # Since we know the structure of the json
            # we can chain the keys to get the temp value
            temp = json_data["main"]["temp"]

            # Convert from Kelvin to Celsius
            celsius_temp = temp - 273.15

            # Convert from Celsius to Fahrenheit
            fahrenheit_temp = (celsius_temp * (9 / 5)) + 32

            # Round values to one decimal place
            celsius_temp = round(celsius_temp, 1)
            fahrenheit_temp = round(fahrenheit_temp, 1)

            result_label.config(text=f"Current temperature in {city}: {fahrenheit_temp}℉ / {celsius_temp}℃")

            # Display temperature
            return f"Current temperature in {city}: {fahrenheit_temp}℉"
            # return f"Current temperature in {city}: {celsius_temp}℃"

        else:
            print(f"Error: {request.status_code}")
            return None
    except Exception as e:
        result_label.config(text=f"An error occured: {e}")

if __name__ == "__main__":
    gui()

    # # Get city name
    # city = input("Enter City: ")
    #
    # temperature = get_temperature(city)
    #
    # if temperature:
    #     print(temperature)
    # else:
    #     print("Failed to retrieve temperature.")





