import geopy.distance
import requests

def find_coordenates(address):
    base_url = "https://nominatim.openstreetmap.org/search"
    headers = {
        'User-Agent': 'distance_finder/1.0'
    }
    payload = {'q': address, 'format': 'json'}
    response = requests.get(base_url, params=payload, headers=headers)
    response_json = response.json()
    return (float(response_json[0]['lat']), float(response_json[0]['lon']))
    
def find_distance(source, destination):
    source_coordinates = find_coordenates(source)
    destination_coordinates = find_coordenates(destination)
    return round(geopy.distance.distance(source_coordinates, destination_coordinates).km, 2)