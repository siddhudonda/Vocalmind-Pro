from core.audio_processor import audio_to_text
from core.llm_engine import query_llm
from core.text_cleaner import clean_text

def test_query_response():
    sample_text = "Tell me a joke"
    response = query_llm(sample_text)
    assert isinstance(response, str) and len(response) > 0
