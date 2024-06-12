import requests
from fastapi import HTTPException
from app.config import settings


GOOGLE_MAP_API_KEY = settings.GOOGLE_MAP_API_KEY

def get_maps_url(location: str) -> str:
    geocode_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={location}&key={GOOGLE_MAP_API_KEY}"
    response = requests.get(geocode_url)
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Error contacting Google Maps API")
    data = response.json()
    if not data['results']:
        raise HTTPException(status_code=400, detail="Invalid location")
    lat_lng = data['results'][0]['geometry']['location']
    return f"https://www.google.com/maps/search/?api=1&query={lat_lng['lat']},{lat_lng['lng']}"