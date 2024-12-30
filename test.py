import requests

def get_weather(city_name, api_key):
    base_url = "http://api.weatherstack.com/current"
    params = {
        'access_key': api_key,  # Replace with your Weatherstack API key
        'query': city_name
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        temperature = data['current']['temperature']
        weather_description = data['current']['weather_descriptions'][0]
        humidity = data['current']['humidity']
        wind_speed = data['current']['wind_speed']
        
        return {
            'weather': weather_description,
            'temperature': temperature,
            'humidity': humidity,
            'wind_speed': wind_speed
        }
    else:
        return {"error": f"Failed to fetch data. Status code: {response.status_code}"}

# Example usage
city = "London"
api_key = "05a5f4a80dba055badc6bf9a980df7ba"  # Replace with your Weatherstack API key
weather_data = get_weather(city, api_key)

if 'error' in weather_data:
    print(weather_data['error'])
else:
    print(f"Weather in {city}: {weather_data['weather']}")
    print(f"Temperature: {weather_data['temperature']}°C")
    print(f"Humidity: {weather_data['humidity']}%")
    print(f"Wind Speed: {weather_data['wind_speed']} km/h")