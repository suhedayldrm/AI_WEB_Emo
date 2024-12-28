# anonymize.py
# Anonymization of data. Removing emails, names, URL's, Phone numbers and other sensitive information

import re
import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

def anonymize_text(text):
    # Remove email addresses
    text = re.sub(r'\S+@\S+', r'\[email\]', text)

    # Anonymize names (assuming capitalized words are names - not 100% accurate)
    text = re.sub(r'\b[A-Z][a-z]+\b', r'\[name\]', text)
    
    # Remove URLs
    text = re.sub(r'http\S+', r'\[url\]', text)
    
    # Anonymize phone numbers (simple format)
    text = re.sub(r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b', r'\[phone\]', text)
    
    # Use spaCy to identify and replace entities
    doc = nlp(text)
    anonymized_text = []
    for ent in doc.ents:
        if ent.label_ in ["PERSON", "NORP", "FAC", "ORG", "GPE", "LOC", "PRODUCT", "EVENT", "WORK_OF_ART", "LAW"]:
            #text = text.replace(ent.text, f'[{ent.label_}]')
            text = text.replace(ent.text, f'[{ent.label_.lower()}]')


    return text