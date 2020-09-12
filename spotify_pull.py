import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import matplotlib.pyplot as plt

# Client ID
cid ="4a7c6a8ab962478687646d76531811d0"

# Secret ID
secret = "a8eebb34f19e4494a93cbd05b772e7cc"

# Authorization Manager
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)

# Access the API with these credentials
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

genre_list = ["yacht-rock", "pop", "country", "hip-hop", "indie-pop", "jazz", "edm", "metal", "punk", "classical"]

for genre in genre_list:
    # create empty lists where the results are going to be stored
    artist_name = []
    track_name = []
    popularity = []
    track_id = []

    for i in range(0,2000,50):
        track_results = sp.search(q='year:2019 genre:'+genre, type='track', market='US',limit=50,offset=i)
        for i, t in enumerate(track_results['tracks']['items']):
            artist_name.append(t['artists'][0]['name'])
            track_name.append(t['name'])
            track_id.append(t['id'])
            popularity.append(t['popularity'])

    df_tracks = pd.DataFrame(
        {'artist_name': artist_name, 'track_name': track_name, 'track_id': track_id, 'popularity': popularity})
    df_tracks.to_csv('./data/' + genre + '.csv')
    print(genre + ' completed!')
    plt.hist(x=popularity, bins=50);
    plt.savefig('./hist/' + genre + '.png')
    plt.clf()