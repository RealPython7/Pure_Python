import requests

BASE_URL = "http://127.0.0.1:8000/"
Endpoint = "json"

resp = requests.get(BASE_URL + Endpoint)

print(resp.json())
print(type(resp))