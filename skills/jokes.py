# skills/jokes.py
import random

jokes_list = [
    "Why did the developer go broke? Because he used up all his cache!",
    "Why do Python developers wear glasses? Because they can't C.",
    "What’s a computer’s least favorite food? Spam."
]

def handle_intent(_text):
    return random.choice(jokes_list)
