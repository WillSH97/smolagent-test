import pyjokes
import random
import requests

from smolagents import tool

@tool
def generate_joke() -> str:
    '''
    This is a tool that returns a random silly joke.
    '''
    return pyjokes.get_joke()

@tool
def return_random_emoji() -> str:
    '''
    This is a tool that returns a random emoji.
    '''
    emoji_list = ["😀", "🚀", "🍕", "🎉", "🐱", "💡", "🌴"]
    return random.choice(emoji_list)

@tool
def get_location():
    '''
    This tool uses ipapi.co to return approximate location information based on IP address.
    '''
    try:
        # Using a free IP geolocation service
        response = requests.get('http://ip-api.com/json/')
        print(response)
        data = response.json()
        print(data)
        return(f"City: {data.get('city')}, Region: {data.get('region')}, Country: {data.get('country')}, Latitude: {data.get('lat')}, Longitude: {data.get('lon')}")
    except Exception as e:
        return (f"Error retrieving location: {e}")