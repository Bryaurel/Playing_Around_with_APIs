#!/usr/bin/env python3
import requests

def get_song_lyrics(song_title):
    urls = [
        "https://genius-song-lyrics1.p.rapidapi.com/song/lyrics/",
        "https://genius-song-lyrics1.p.rapidapi.com/search/",
        "https://genius-song-lyrics1.p.rapidapi.com/artist/details/",
        "https://genius-song-lyrics1.p.rapidapi.com/artist/songs/",
        "https://genius-song-lyrics1.p.rapidapi.com/song/details/"
    ]
    
    querystring = {"q": song_title, "per_page": "1", "page": "1"}
    
    headers = {
        "X-RapidAPI-Key": "5d70b22ceemshd6f5559bbad3234p1be2e0jsn556e0e486a85",
        "X-RapidAPI-Host": "genius-song-lyrics1.p.rapidapi.com"
    }
    
    for url in urls:
        response = requests.get(url, headers=headers, params=querystring)
    
        if response.status_code == 200:
            data = response.json()
            if data.get('response'):
                song_data = data['response']['hits'][0]['result']
                
            
                if 'lyrics_path' in song_data:
                    lyrics_url = "https://genius-song-lyrics1.p.rapidapi.com" + song_data['lyrics_path']
                    lyrics_response = requests.get(lyrics_url, headers=headers)
                    lyrics_data = lyrics_response.json()
                    song_data['lyrics'] = lyrics_data['response']['lyrics']
                
                return song_data
        else:
            print("Error with the API request:", response.status_code)
            return None

if __name__ == "__main__":
    song_title = input("Enter a song title : ")
    song_data = get_song_lyrics(song_title)
    
    if song_data:
        print("Title of the song :", song_data['title'])
        print("Artist :", song_data['primary_artist']['name'])
        if 'lyrics' in song_data:
            print("Lyrics :", song_data['lyrics'])
    else:
        print("No song found.")
