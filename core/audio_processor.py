# core/audio_processor.py
import speech_recognition as sr

def audio_to_text(audio_file, language="te-IN"):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)
        return recognizer.recognize_google(audio, language=language)
    except:
        return ""
