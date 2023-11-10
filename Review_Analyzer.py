import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import nltk  # Natural Language Processing Toolkit
from nltk.corpus import stopwords
import re  # Natural Language Processing Toolkit
from textblob import TextBlob # Python library for Sentiment analysis 

# Stopwords for preprocessing
nltk.download('stopwords')
nltk.download('punkt')
all_stopwords = stopwords.words('english')
all_stopwords.remove('not')

def text_preprocessor(text):

    # To pre process text reviews
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.lower()
    a = [w for w in nltk.word_tokenize(text) if w not in all_stopwords]
    return ' '.join(a)

def get_sentiment(text):

    # To analyze single review
    text = text_preprocessor(text)
    blob = TextBlob(text)
    
    polarity = round(blob.sentiment.polarity, 2)
    subjectivity = round(blob.sentiment.subjectivity, 2)
    
    if polarity >= 0.3:
        sentiment = 'Positive'
    elif polarity <= 0.:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    
    return polarity, subjectivity, sentiment



def analyze_data(file_path, file_format='csv'):

    # Read data based on the specified file format
    if file_format == 'csv':
        data = pd.read_csv(file_path)
    elif file_format == 'excel':
        data = pd.read_excel(file_path)
    elif file_format == 'parquet':
        data = pd.read_parquet(file_path)

    # Sentiment analysis
    sentiment = []
    subjectivity = []
    polarity = []

    preprocessed_data = data
    preprocessed_data['Review'].apply(text_preprocessor)

    for text in preprocessed_data['Review']:
        pol, subj, sent = get_sentiment(text)
        polarity.append(pol)
        subjectivity.append(subj)
        sentiment.append(sent)

    data['Polarity'] = polarity
    data['Sentiment'] = sentiment
    data['Subjectivity'] = subjectivity

    return data