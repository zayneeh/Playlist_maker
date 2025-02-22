from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

class SpotifyClient:
    def __init__(self, client_id: str, client_secret: str, redirect_uri: str):
        self.spotify = Spotify(auth_manager=SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope="playlist-read-private playlist-read-collaborative"
        ))

    def get_playlist_tracks(self, playlist_url: str):
        # Extract playlist ID from URL
        playlist_id = playlist_url.split('/')[-1].split('?')[0]
        
        tracks = []
        results = self.spotify.playlist_tracks(playlist_id)
        
        while results:
            for item in results['items']:
                if item['track']:
                    track = item['track']
                    tracks.append({
                        'title': track['name'],
                        'artists': [artist['name'] for artist in track['artists']],
                        'duration_ms': track['duration_ms'],
                        'album': track['album']['name']
                    })
            results = self.spotify.next(results) if results['next'] else None
            
        return tracks