import gradio as gr
from core.audio_processor import audio_to_text
from core.llm_engine import query_llm
from core.text_cleaner import clean_text
from core.voice_generator import text_to_speech
from core.intent_parser import parse_intent
from skills import jokes, news, calculator, dictionary


def process_audio(audio_path, mode='normal'):
    if not audio_path:
        return "No audio received", None

    text = audio_to_text(audio_path)
    if not text:
        return "Could not understand audio", None

    if mode == 'elderly':
        text = f"This is a query from an elderly person: {text}"
    elif mode == 'kids':
        text = f"This is a kid asking: {text}"

    intent = parse_intent(text)

    # Skill routing (simplified)
    if intent == "joke":
        response = jokes.tell_joke()
    elif intent == "news":
        response = news.get_latest_news()
    elif intent == "calc":
        response = calculator.solve(text)
    elif intent == "define":
        response = dictionary.define(text)
    else:
        response = query_llm(text)

    cleaned = clean_text(response)
    audio_file = text_to_speech(cleaned)
    return cleaned, audio_file


def run_app():
    with gr.Blocks() as demo:
        gr.Markdown("# VocalMind Pro - Multilingual Voice Assistant")

        with gr.Row():
            audio_input = gr.Audio(sources="microphone", type="filepath", label="Speak now")
            mode_selector = gr.Dropdown(choices=["Normal", "Elderly", "Kids"], value="Normal", label="Select Mode")

        with gr.Row():
            text_output = gr.Textbox(label="Text Response")
            audio_output = gr.Audio(label="Audio Response", type="filepath")

        def wrapped(audio, mode):
            return process_audio(audio, mode.lower())

        audio_input.change(wrapped, inputs=[audio_input, mode_selector], outputs=[text_output, audio_output])

    demo.launch(debug=True, share=True)


if __name__ == '__main__':
    run_app()