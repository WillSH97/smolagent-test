import pyjokes
import random

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