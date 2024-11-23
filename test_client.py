from client_library import TranslationClient

client = TranslationClient(base_url="http://127.0.0.1:8000", max_retries=10, backoff_factor=1.25, timeout=10, debug=False)

try:
    status = client.get_status()
    print(f"Final job status: {status}")
    
    cached_status = client.get_cached_status()
    print(f"Cached job status: {cached_status}")
    
except TimeoutError as e:
    print(f"Timeout occurred: {e}")
except Exception as e:
    print(f"Error occurred: {e}")
