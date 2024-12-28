import re
import spacy

# Precompile regular expressions
email_regex = re.compile(r'\S+@\S+')
url_regex = re.compile(r'http\S+')
phone_regex = re.compile(r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b')
name_regex = re.compile(r'\b[A-Z][a-z]+\b')

# Load the spaCy model outside the function
nlp = spacy.load("en_core_web_sm")

def anonymize_text(text, nlp_model):
    # Use compiled regex for replacements
    text = email_regex.sub(r'[email]', text)
    text = name_regex.sub(r'[name]', text)
    text = url_regex.sub(r'[url]', text)
    text = phone_regex.sub(r'[phone]', text)

    # Use spaCy for entity replacement
    doc = nlp_model(text)
    replacements = [(ent.start_char, ent.end_char, f'[{ent.label_.lower()}]') for ent in doc.ents if ent.label_ in ["PERSON", "NORP", "FAC", "ORG", "GPE", "LOC", "PRODUCT", "EVENT", "WORK_OF_ART", "LAW"]]
    
    # Reconstruct text from segments
    last_end = 0
    segments = []
    for start, end, replacement in replacements:
        segments.append(text[last_end:start])
        segments.append(replacement)
        last_end = end
    segments.append(text[last_end:])
    
    return ''.join(segments)
