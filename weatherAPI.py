import requests

def get_weather_data(latitude, longitude, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/onecall"
    params = {
        "lat": latitude,
        "lon": longitude,
        "appid": api_key,
        "units": "metric"  # You can change the units as needed
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code)
        return None

def main():
    # Example coordinates (latitude and longitude)
    latitude = 37.7749
    longitude = -122.4194
    
    # Your OpenWeatherMap API key
    api_key = ""
    
    weather_data = get_weather_data(latitude, longitude, api_key)
    if weather_data:
        # Do something with the weather data
        print(weather_data)
    else:
        print("Failed to retrieve weather data.")

if __name__ == "__main__":
    main()
