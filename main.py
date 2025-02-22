from config import Config
from clients.spotify import SpotifyClient
from clients.ytmusic import YTMusicClient
from converter import PlaylistConverter
from utils import setup_logging

def main():
    # Setup logging
    logger = setup_logging()
    
    try:
        # Load configuration
        config = Config()
        
        # Initialize clients
        spotify_client = SpotifyClient(
            config.spotify_client_id,
            config.spotify_client_secret,
            config.spotify_redirect_uri
        )
        ytmusic_client = YTMusicClient()
        
        # Create converter
        converter = PlaylistConverter(spotify_client, ytmusic_client)
        
        # Get user input
        spotify_url = input("Enter Spotify playlist URL: ")
        playlist_name = input("Enter name for YouTube Music playlist: ")
        
        # Convert playlist
        playlist_id, successful, total = converter.convert_playlist(
            spotify_url,
            playlist_name
        )
        
        # Print results
        print(f"\nPlaylist conversion completed!")
        print(f"YouTube Music Playlist ID: {playlist_id}")
        print(f"Successfully converted {successful} out of {total} tracks")
        
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        raise

if __name__ == "__main__":
    main()
