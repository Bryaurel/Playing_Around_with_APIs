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
    
    if song_title = Despacito
       print("Ay (Fonsi, DY)
(Oh, oh) oh, no, oh no (oh)
Hey, yeah, diri-diri-diriridi, Daddy, go!
Sí, sabes que ya llevo un rato mirándote
Tengo que bailar contigo hoy (DY)
Vi que tu mirada ya estaba llamándome
Muéstrame el camino, que yo voy (oh)
Tú, tú eres el imán y yo soy el metal
Me voy acercando y voy armando el plan
Solo con pensarlo se acelera el pulso (oh, yeah)
Ya, ya me estás gustando más de lo normal
Todos mis sentidos van pidiendo más
Esto hay que tomarlo sin ningún apuro
Despacito
Quiero respirar tu cuello despacito
Deja que te diga cosas al oído
Para que te acuerdes si no estás conmigo
Despacito
Quiero desnudarte a besos, despacito
Firmar las paredes de tu laberinto
Y hacer de tu cuerpo todo un manuscrito (sube, sube, sube)
Sube, sube (oh)
Quiero ver bailar tu pelo, quiero ser tu ritmo
Que le enseñes a mi boca tus lugares favoritos
(Favoritos, favoritos, baby)
Déjame sobrepasar tus zonas de peligro
Hasta provocar tus gritos y que olvides tu apellido
Si te pido un beso, ven, dámelo
Yo sé que estás pensándolo
Llevo tiempo intentándolo
Mami, esto es dando y dándolo
Sabes que tu corazón conmigo te hace bam-bam
Sabes que esa beba está buscando de mi bam-bam
Ven, prueba de mi boca para ver cómo te sabe
Quiero, quiero, quiero ver cuánto amor a ti te cabe
Yo no tengo prisa, yo me quiero dar el viaje
Empezamos lento, después salvaje
Pasito a pasito, suave, suavecito
Nos vamos pegando poquito a poquito
Cuando tú me besas con esa destreza
Veo que eres malicia con delicadeza
Pasito a pasito, suave, suavecito
Nos vamos pegando poquito a poquito
Y es que esa belleza es un rompecabezas
Pero pa' montarlo, aquí tengo la pieza, oye
Despacito
Quiero respirar tu cuello despacito
Deja que te diga cosas al oído
Para que te acuerdes si no estás conmigo
Despacito
Quiero desnudarte a besos despacito
Firmar las paredes de tu laberinto
Y hacer de tu cuerpo todo un manuscrito (sube, sube, sube)
Sube, sube (oh)
Quiero ver bailar tu pelo, quiero ser tu ritmo
Que le enseñes a mi boca tus lugares favoritos
(Favoritos, favoritos, baby)
Déjame sobrepasar tus zonas de peligro
Hasta provocar tus gritos y que olvides tu apellido
Despacito
Vamo' a hacerlo en una playa en Puerto Rico
Hasta que las olas griten: ¡ay, Bendito
Para que mi sello se quede contigo (báilalo)
Pasito a pasito, suave, suavecito
Nos vamos pegando poquito a poquito
Que le enseñes a mi boca tus lugares favoritos
(Favoritos, favoritos, baby)
Pasito a pasito, suave, suavecito
Nos vamos pegando poquito a poquito
Hasta provocar tus gritos y que olvides tu apellido (DY)
Despacito")
    elif song_data:
        print("Title of the song :", song_data['title'])
        print("Artist :", song_data['primary_artist']['name'])
        if 'lyrics' in song_data:
            print("Lyrics :", song_data['lyrics'])
    else:
        print("No song found.")
