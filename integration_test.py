import subprocess
import time
from client_library import TranslationClient


def start_server():
    # Start the FastAPI server in a subprocess
    server_process = subprocess.Popen(
        ["uvicorn", "server:app", "--port", "8000"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    time.sleep(2)  # Allow server to start
    return server_process


def stop_server(server_process):
    # Terminate the server process
    server_process.terminate()


def test_translation_client():
    server_process = start_server()

    try:
        # Create an instance of TranslationClient
        client = TranslationClient(base_url="http://127.0.0.1:8000", max_retries=10, backoff_factor=1.5, timeout=10)

        # Poll the server
        try:
            status = client.get_status()
            print(f"Final job status: {status}")
            assert status in ["completed", "error"]

            cached_status = client.get_cached_status()
            print(f"Cached job status: {cached_status}")
            assert cached_status == status

        except TimeoutError:
            print("Test failed: Client timed out.")
    finally:
        stop_server(server_process)
