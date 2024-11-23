import requests
import logging
import time

logging.basicConfig(level=logging.INFO)

class TranslationClient:
    def __init__(self, base_url: str, max_retries: int = 10, backoff_factor: float = 1.5, timeout: int = 30, debug: bool = False):
        self.base_url = base_url
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor
        self.timeout = timeout
        self.last_known_state = None

        self.logger = logging.getLogger(__name__)
        if debug:
            logging.basicConfig(level=logging.INFO)
        else:
            logging.basicConfig(level=logging.WARNING)

    def get_status(self, endpoint: str = "/status") -> str:
        attempt = 0

        while attempt < self.max_retries:
            try:
                response = requests.get(f"{self.base_url}{endpoint}", timeout=self.timeout)
                response.raise_for_status()
                status = response.json().get("result")

                self.logger.info(f"Attempt {attempt + 1}: Received status '{status}'")

                if status in ["completed", "error"]:
                    self.last_known_state = status
                    return status

                time.sleep(self.backoff_factor ** attempt)
                attempt += 1

            except requests.Timeout:
                self.logger.error("Request timed out. Retrying...")
            except requests.ConnectionError:
                self.logger.error("Connection error occurred. Retrying...")
            except requests.RequestException as e:
                self.logger.error(f"General error: {e}")

            time.sleep(self.backoff_factor ** attempt)
            attempt += 1

        raise TimeoutError("Max retries reached without resolving the job status")
    
    def get_cached_status(self) -> str:
        if self.last_known_state:
            logging.info(f"Returning cached status: {self.last_known_state}")
            return self.last_known_state
        else:
            logging.warning("No cached status available.")
            return "unknown"