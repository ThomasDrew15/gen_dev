import requests

def get_current_weather(latitude, longitude, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
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
    # User input for latitude and longitude
    latitude = float(input("Enter latitude: "))
    longitude = float(input("Enter longitude: "))
    
    # Your OpenWeatherMap API key
    api_key = ""
    
    current_weather = get_current_weather(latitude, longitude, api_key)
    if current_weather:
        # Do something with the current weather data
        print(current_weather)
    else:
        print("Failed to retrieve current weather data.")

if __name__ == "__main__":
    main()
