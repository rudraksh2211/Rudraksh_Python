import requests

def weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=997ea71a831f55cd3f76fc2e4c3c3eea"
    try:
        response = requests.get(url)
        data = response.json()
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        feels_like = data["main"]["feels_like"]
        wind = data["wind"]["speed"]
        pressure=data["main"]["pressure"]
        
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C (Feels like: {feels_like}°C)")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind}kph")
        print(f"Pressure: {pressure}hpa")
        print(f"Description: {data["weather"][0]["description"].capitalize()}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")

city = input("Enter City: ")
weather(city)
