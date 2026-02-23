# text processing libraries:
import nltk
nltk.download('punkt_tab')
nltk.download("punkt")
nltk.download("stopwords")
nltk.download('wordnet')
# for tokenization
from nltk.tokenize import word_tokenize
#for removing stopwords
from nltk.corpus import stopwords
#for stemming and lemmatization
from nltk.stem import WordNetLemmatizer
#import sklearn dependencies
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import string 
#libraries done



#data
training_data = [
  
("Hello","greet"),("hi there","greet"),("how are you",    "greet"),("good morning","greet"),("good night","greet"),("hey","greet"),
                 
("what's the weather today","weather"),("tell me weather","weather"),("is it going to rain today","weather"),("is it raining","weather"),("do I need an umbrella","weather"),("what's the temperature","weather"),

("open","open_app"),("launch","open_app"),("start","open_app"),("run","open_app"),("execute","open_app"),("begin","open_app"),("open google","open_app"),("launch youtube","open_app"),("start spotify","open_app"),("run calculator","open_app"),("execute notepad","open_app"),("begin word","open_app"),

("bye","exit"),("goodbye","exit"),("see you later","exit"),("farewell","exit"),("take care","exit"),("have a nice day","exit"),

("I am sad","sadness"),("I am feeling down","sadness"),("I am unhappy","sadness"),("I am depressed","sadness"),("I am not feeling well","sadness"),

("I am happy","happiness"),("I am feeling great","happiness"),("I am joyful","happiness"),("I am excited","happiness"),("I am having fun","happiness"),

("What is your name?","name_query"),("Who are you?","name_query"),("Can you tell me your name?","name_query"),("May I know your name?","name_query"),("Could you please tell me your name?","name_query")]


sentences = []
labels = []

for text, intent in training_data:
  sentences.append(text)
  labels.append(intent)



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

def preprocess_text(sentences):
  for sentence in sentences:
    cleaned_sentences.append(preprocess(sentence))
  return cleaned_sentences
#print(preprocess_text(sentences))

clean_data = preprocess_text(sentences)

#data cleaned and preprocessed, now we will convert it to features using TF-IDF vectorizer


vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(clean_data)
Y = labels


#model training
model = LogisticRegression()
model.fit(X, Y)