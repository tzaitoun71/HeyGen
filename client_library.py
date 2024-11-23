import requests
import logging

logging.basicConfig(level=logging.INFO)

class TranslationClient:
    def __init__(self, base_url: str,):
        self.base_url = base_url

    def get_status(self, endpoint: str = "/status") -> str:
        response = requests.get(f"{self.base_url}{endpoint}")
        response.raise_for_status()
        status = response.json().get("result")
        return status