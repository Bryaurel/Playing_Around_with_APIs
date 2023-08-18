#!/usr/bin/env python3
import requests

url = "https://genius-song-lyrics1.p.rapidapi.com/search/"

querystring = {"q":"<REQUIRED>","per_page":"10","page":"1"}

headers = {
	"X-RapidAPI-Key": "5d70b22ceemshd6f5559bbad3234p1be2e0jsn556e0e486a85",
	"X-RapidAPI-Host": "genius-song-lyrics1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
