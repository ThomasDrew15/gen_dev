from geopy.geocoders import Nominatim


def get_gps_coordinates(address):
    geolocator = Nominatim(user_agent="uniqueName")
    location = geolocator.geocode(address)
    
    if location:
        latitude = location.latitude
        longitude = location.longitude
        return latitude, longitude
    else:
        return None


if __name__ == "__main__":
    
    address = "Newton Abbot"
    
    coordinates = get_gps_coordinates(address)
    
    if coordinates:
        latitude, longitude = coordinates
        print(f"Latitude: {latitude}, Longitude: {longitude}")
    else:
        print("Location not found.")