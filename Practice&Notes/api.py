print("Running api.py")

import requests
print("Running api.py")
def weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    try:
        response = requests.get(url)
        data = response.json()
        print(data)  # You can print specific data as well, like temperature
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")

city = input("Enter City: ")
weather(city, "997ea71a831f55cd3f76fc2e4c3c3eea")
