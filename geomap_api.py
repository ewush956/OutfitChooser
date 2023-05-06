from geomap_key import API_KEY
import requests

def get_lat_lng(location: str) -> dict:
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    query_parameters = {
        "address": location,
        "key": API_KEY,
        }
        
    response = requests.get(url, params=query_parameters)
    response.raise_for_status()

    result = response.json()["results"][0]
    lat = result["geometry"]["location"]["lat"]
    lng = result["geometry"]["location"]["lng"]
    return