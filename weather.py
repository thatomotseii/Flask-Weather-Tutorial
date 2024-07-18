from dotenv import load_dotenv
from pprint import pprint
import requests
import os

# Load environment variables from a .env file
load_dotenv()

def get_current_weather(city="Bloemfontein"):
    # Get the API key from the environment variable
    api_key = os.getenv("API_KEY")
    
    if not api_key:
        raise ValueError("No API key found. Please set the API_KEY environment variable.")
    
    # Form the request URL
    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}&units=imperial'
    
    # Make the request to the API
    response = requests.get(request_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Could not retrieve weather data"}

if __name__ == "__main__":
    print("\n** Get Current Weather Conditions **\n")
    city = input("\nPlease enter city name: ")
    if not bool(city.strip()):
        city="Bloemfontein"
    
    weather_data = get_current_weather(city)
    
    print("\n")
    pprint(weather_data)
