# core/text_cleaner.py
import re

def clean_text(text):
    return re.sub(r"[#*]", "", text)
