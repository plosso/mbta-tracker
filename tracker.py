import requests
import json

resp = requests.get("https://api-v3.mbta.com/stops?filter[route]=Red,Orange,Blue")

print(resp.json())