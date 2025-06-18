import requests

def define(query):
    """Fetch definition from a dictionary API."""
    try:
        word = query.split("define")[-1].strip()
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        response = requests.get(url).json()
        definition = response[0]['meanings'][0]['definitions'][0]['definition']
        return f"{word.capitalize()} means: {definition}"
    except Exception as e:
        return "Sorry, I couldn't find the definition."
