# core/voice_generator.py
from gtts import gTTS

def text_to_speech(text, language='te'):
    try:
        tts = gTTS(text=text, lang=language)
        output_path = "outputs/response_te.mp3"
        tts.save(output_path)
        return output_path
    except Exception as e:
        print(f"TTS Error: {e}")
        return None
