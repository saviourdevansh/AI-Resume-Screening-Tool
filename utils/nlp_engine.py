import spacy

# Load model only once
nlp = spacy.load("en_core_web_sm")


def process_text(text):
    return nlp(text)


def get_nlp():
    return nlp