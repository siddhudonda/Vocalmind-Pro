# core/intent_parser.py
def classify_intent(text: str) -> str:
    text = text.lower()

    if "joke" in text:
        return "joke"
    elif "weather" in text:
        return "weather"
    elif "calculate" in text or any(c in text for c in "+-*/="):
        return "calculator"
    elif "translate" in text:
        return "translate"
    elif "meaning" in text or "define" in text:
        return "dictionary"
    return "general"
