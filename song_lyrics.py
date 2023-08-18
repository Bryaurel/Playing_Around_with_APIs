#!/usr/bin/env python3
import requests

def get_song_lyrics(song_title):
    url = "https://genius-song-lyrics1.p.rapidapi.com/search/"
    
    querystring = {"q": song_title, "per_page": "1", "page": "1"}
    
    headers = {
        "X-RapidAPI-Key": "5d70b22ceemshd6f5559bbad3234p1be2e0jsn556e0e486a85",
        "X-RapidAPI-Host": "genius-song-lyrics1.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers, params=querystring)
    
    if response.status_code == 200:
        data = response.json()
        if data.get('response'):
            song_data = data['response']['hits'][0]['result']
            return song_data
        else:
            return None
    else:
        print("Error with the API request:", response.status_code)
        return None

if __name__ == "__main__":
    song_title = input("Enter a song title : ")
    song_data = get_song_lyrics(song_title)
    
    if song_data:
        print("Title of the song :", song_data['title'])
        print("Artist :", song_data['primary_artist']['name'])
    else:
        print("No song found.")

