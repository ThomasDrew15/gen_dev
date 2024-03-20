from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

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
        return {"error": f"Failed to retrieve data. Status code: {response.status_code}"}

@app.route('/weather', methods=['GET'])
def weather():
    latitude = request.args.get('lat', type=float)
    longitude = request.args.get('lon', type=float)
    api_key = "YOUR_API_KEY_HERE"  # Replace YOUR_API_KEY_HERE with your actual API key

    # Ensure both latitude and longitude are provided
    if latitude is None or longitude is None:
        return jsonify({"error": "Please provide both latitude and longitude."}), 400

    current_weather = get_current_weather(latitude, longitude, api_key)
    return jsonify(current_weather)

if __name__ == "__main__":
    app.run(debug=True)
