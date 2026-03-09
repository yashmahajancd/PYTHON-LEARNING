import requests
try:
    response = requests.get("https://api.github.com", timeout=5)
    response.raise_for_status()  # Raise exception for bad status codes
    print(response.status_code)
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")