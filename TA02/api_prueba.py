import requests

API_KEY = "Hb2ZG7YNBMC59SiZKEvMLnqCgvY8JkL69V6CrECz"

url = "https://api.api-ninjas.com/v2/carfacets"
params = {
    "make": "BMW",
    "model": "4 Series",
    "facets": "body,fuel,transmission,year",  # what you want counts for
}
headers = {"X-Api-Key": API_KEY}

response = requests.get(url, params=params, headers=headers)

if response.status_code == requests.codes.ok:
    print(response.json())
else:
    print("Error:", response.status_code, response.text)