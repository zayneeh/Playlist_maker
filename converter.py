# converter.py
from clients.spotify import SpotifyClient
from clients.ytmusic import YTMusicClient
import logging

logger = logging.getLogger(__name__)

class PlaylistConverter:
    def __init__(self, spotify_client: SpotifyClient, ytmusic_client: YTMusicClient):
        self.spotify = spotify_client
        self.ytmusic = ytmusic_client

    def convert_playlist(self, spotify_url: str, ytmusic_playlist_name: str):
        # Get tracks from Spotify
        logger.info("Fetching Spotify tracks...")
        spotify_tracks = self.spotify.get_playlist_tracks(spotify_url)
        
        # Create YouTube Music playlist
        logger.info("Creating YouTube Music playlist...")
        playlist_id = self.ytmusic.create_playlist(
            ytmusic_playlist_name,
            "Converted from Spotify playlist"
        )
        
        # Convert tracks
        successful = 0
        total = len(spotify_tracks)
        
        for track in spotify_tracks:
            logger.info(f"Processing: {track['title']} by {track['artists'][0]}")
            
            # Search for song on YouTube Music
            result = self.ytmusic.search_song(track['title'], track['artists'][0])
            
            if result:
                # Add to playlist
                self.ytmusic.add_to_playlist(playlist_id, result['videoId'])
                successful += 1
                logger.info(f"Added successfully: {track['title']}")
            else:
                logger.warning(f"Could not find: {track['title']}")
        
        return playlist_id, successful, total