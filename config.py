import json
from pathlib import Path

class Config:
    def __init__(self, config_path: str = "config.json"):
        self.config_path = Path(config_path)
        self._load_config()
    
    def _load_config(self):
        with open(self.config_path) as f:
            self._config = json.load(f)
            
        self.spotify_client_id = self._config["spotify_client_id"]
        self.spotify_client_secret = self._config["spotify_client_secret"]
        self.spotify_redirect_uri = self._config["spotify_redirect_uri"]