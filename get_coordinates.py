import requests

def get_coordinates(city, country):
    url = f"https://nominatim.openstreetmap.org/search?q={city},{country}&format=json"
    response = requests.get(url).json()
    if response:
        return response[0]['lat'], response[0]['lon']
    else:
        return None

latitude, longitude = get_coordinates("Nablus", "Palestine")
print(f"Latitude: {latitude}, Longitude: {longitude}")
