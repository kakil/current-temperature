from dotenv import load_dotenv
import os
import requests
import json


load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")

# How to make a call using open weather map api
# http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={API key}
#
# API Call for city name:
# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

# Get city name
city = input("Enter City: ")

request = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")
json_data = request.json()
print(json_data)

# Get temp value
# Since we know the structure of the json
# we can chain the keys to get the temp value
temp = json_data["main"]["temp"]

# Convert from Kelvin to Celsius
celsius_temp = temp - 273.15

# Convert from Celsius to Fahrenheit
fahrenheit_temp = (celsius_temp * (9/5)) + 32

# Round values to one decimal place
celsius_temp = round(celsius_temp, 1)
fahrenheit_temp = round(fahrenheit_temp, 1)

# Display temperature
print(f"Current temperature in {city}: {fahrenheit_temp}℉")
print(f"Current temperature in {city}: {celsius_temp}℃")


