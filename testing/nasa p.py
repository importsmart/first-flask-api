import requests, json

response = requests.get("https://api.nasa.gov/planetary/apod?api_key=YV5qKOZHskncZ7HiZgw90jdXODbXijaXkdvLHol7")
print(response.status_code)

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent = 4)
    print(text)

jprint(response.json())

url = response.json()['url']
title = response.json()['title']
exp = response.json()['explanation']