# Translation Client Library

This Python client library interacts with a simulated video translation server. It provides an efficient way to track the progress of video translation jobs with retries, exponential backoff, logging, and caching.

---

## Installation

1. **Clone the repository**  
   Use the following command to clone the repository:
   ```bash
   git clone https://github.com/github_username/Translation-Client-Library.git

2. **Navigate to the project folder**
   Change your directory to the cloned repository:
   ```bash
   cd Translation-Client-Library

3. **Install the required dependencies**
   run the following command to install all dependencies:
   ```bash
   pip install -r requirements.txt

4. **Start the FastAPI server**
   To start the server, use the following command:
   ```bash
   uvicorn server:app --port 8000

---

# How to Use the TranslationClient Library

1. **Import the Library**  
   Import the `TranslationClient` in your Python script:
   ```python
   from client_library import TranslationClient

2. **Initialize the Client**
   Create an instance of the client:
   ```python
   client = TranslationClient(
    base_url="http://127.0.0.1:8000",  # Server URL
    max_retries=10,                   # Maximum retries
    backoff_factor=1.5,               # Exponential backoff multiplier
    timeout=10,                       # Request timeout
    debug=True                        # Enable detailed logging
   )

3. **Get Job Status**
   Use the `get_status()` method to check the status of the translation job:
   
   ```python
   status = client.get_status()
   print(f"Final job status: {status}")

4. **Retrieve Cached Status**
   Access the cached final status with:
   ```python
   cached_status = client.get_cached_status()
   print(f"Cached job status: {cached_status}")


---

# How to Test the TranslationClient Library
  To ensure the client library works correctly with the server, run the integration tests:
  ```bash
  pytest -s integration_test.py
  ```

  the `-s` flag ensures all logs and print statements appear in the terminal. 


---

# Features of the Translation Client Library

The Translation Client Library is designed to efficiently interact with a simulated video translation server. Below are the key features:


## Key Features

- **Exponential Backoff**  
  Gradually increases the delay between retry attempts to reduce server load and avoid unnecessary network traffic.

- **Retry Mechanism**  
  Automatically retries requests up to a configurable maximum (`max_retries`) in case of failures.

- **Timeout Handling**  
  Ensures the client does not wait indefinitely for a server response by setting a maximum `timeout` duration for each request.

- **Final State Caching**  
  Caches the last known state (`completed` or `error`) for quick access, minimizing redundant server calls.

- **Detailed Logging**  
  Logs all client activity, including retries, errors, and state transitions, to both the console and a file (`translation_client.log`).

- **Configurable Parameters**  
  - `max_retries`: Maximum number of retry attempts.
  - `backoff_factor`: Multiplier for the exponential backoff delay.
  - `timeout`: Maximum wait time for each server response.
  - `debug`: Enables detailed logging for debugging purposes.
