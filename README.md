# Spotify to YouTube Music Playlist Converter

A Python tool to convert Spotify playlists to YouTube Music playlists.

## Setup

1. Install required packages:
```bash
pip install spotipy ytmusicapi
```

2. Create a `config.json` file in the project root:
```json
{
    "spotify_client_id": "your_spotify_client_id",
    "spotify_client_secret": "your_spotify_client_secret",
    "spotify_redirect_uri": "http://localhost:8888/callback"
}
```

3. Set up YouTube Music authentication:
   - Run `ytmusicapi oauth` in your terminal
   - Follow the prompts to authenticate
   - This will create an `oauth.json` file in your project directory

## Getting Spotify Credentials

1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Create a new application
3. Get your Client ID and Client Secret
4. Add `http://localhost:8888/callback` to your Redirect URIs in the app settings

## Usage

1. Navigate to the project directory
2. Run the script:
```bash
python main.py
```
3. Enter the Spotify playlist URL when prompted
4. Enter a name for the new YouTube Music playlist
5. Wait for the conversion to complete

## Notes

- The converter will attempt to find the best match for each track
- Some tracks might not be found if they're not available on YouTube Music
- The script logs all operations and provides a summary at the end
- The created playlist will be private by default

## Troubleshooting

- If authentication fails, ensure your credentials in `config.json` are correct
- If YouTube Music authentication fails, delete `oauth.json` and run setup again
- Check the logs for detailed error messages