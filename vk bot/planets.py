import requests
import json

def get_planet(): 
    api_url = "https://swapi.dev/api/planets"
    response = requests.get(api_url) 
    data = response.json() 
    largest = data["results"][0] 
    for planet in data["results"]: 
        if int(planet["diameter"]) > int(largest["diameter"]): 
            largest = planet 
    return largest["name"]