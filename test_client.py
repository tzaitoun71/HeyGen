from client_library import TranslationClient

client = TranslationClient(base_url="http://127.0.0.1:8000", max_retries=5, backoff_factor=2.0, timeout=10)

try:
    status = client.get_status()
    print(f"Final job status: {status}")
except TimeoutError as e:
    print(f"Timeout occurred: {e}")
except Exception as e:
    print(f"Error occurred: {e}")
