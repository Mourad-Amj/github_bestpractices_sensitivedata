from dotenv import load_dotenv
import os
import requests

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("API_KEY")

def fetch_data_from_api():
    """Fetch data from an example API using the API_KEY."""
    
    url = "https://exampleapi.com/data"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return f"Failed to retrieve data. Status code: {response.status_code}"

if __name__ == "__main__":
    data = fetch_data_from_api()
    print(data)
