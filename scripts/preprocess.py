import re
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def retain_important_numbers(text):
    """
    Retain numbers which are part of sentences while removing standalone numbers.
    """
    return ' '.join([word if (word.isdigit() and len(word) > 1) or not word.isdigit() else '' for word in text.split()])

def lemmatize(text):
    """
    Lemmatize words in the given text using NLTK's WordNetLemmatizer.
    """
    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(text)
    return ' '.join([lemmatizer.lemmatize(i) for i in tokens])

def preprocess_text(text):
    """
    Convert text to lowercase, remove punctuation, stopwords, and lemmatize.
    """
    # Convert to lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    text = ' '.join([i for i in tokens if not i in stop_words])

    # Lemmatize
    text = lemmatize(text)

    # Retain important numbers
    text = retain_important_numbers(text)

    return text
