from client_library import TranslationClient

client = TranslationClient(base_url="http://127.0.0.1:8000")

try:
    status = client.get_status()
    print(f"Job status: {status}")
except Exception as e:
    print(f"Error occurred: {e}")
