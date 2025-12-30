from chatbot.preprocess import clean_text

def test_clean_text():
    assert clean_text("Fever!") == "fever"
