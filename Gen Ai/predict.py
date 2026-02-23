import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import joblib
import string
import pickle as pkl
cleaned_sentences = []
def preprocess(text):
    text = text.lower()
    tokens = word_tokenize(text)
    punc = string.punctuation
    punctuation_filter = [word for word in tokens if word not in punc]
    stop_words = set(stopwords.words("english"))
    stopword_filter = [word for word in punctuation_filter if word not in stop_words]
    wnet = WordNetLemmatizer()
    lemmatized_words = []
    for word in stopword_filter:
        lemmatized_words.append(wnet.lemmatize(word,"v"))
        cleaned_text = " ".join(lemmatized_words)
    return cleaned_text
def predict_intent(user_input):
    vectorizer = joblib.load('tfidf.pkl')
    model = joblib.load('intent_clf_model.pkl')
    
    processed_input = preprocess(user_input)
    user_vector = vectorizer.transform([processed_input])
    prediction = model.predict(user_vector)
    return prediction[0]