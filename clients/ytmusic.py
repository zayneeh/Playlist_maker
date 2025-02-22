from ytmusicapi import YTMusic
import os

class YTMusicClient:
    def __init__(self):
        # Check if oauth.json exists
        if not os.path.exists('oauth.json'):
            print("Setting up YouTube Music authentication...")
            # This will guide you through the auth setup process
            YTMusic.setup(filepath='oauth.json')
        
        self.ytmusic = YTMusic('oauth.json')

    def search_song(self, title: str, artist: str):
        search_results = self.ytmusic.search(f"{title} {artist}", filter="songs")
        return search_results[0] if search_results else None

    def create_playlist(self, name: str, description: str):
        return self.ytmusic.create_playlist(name, description)

    def add_to_playlist(self, playlist_id: str, song_id: str):
        return self.ytmusic.add_playlist_items(playlist_id, [song_id])