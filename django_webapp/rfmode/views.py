from django.shortcuts import render
import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
import joblib
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from newspaper import Article
import nltk
from nltk.corpus import stopwords
import pickle
from textblob import TextBlob


stop_words = stopwords.words('english')

vec_train = pickle.load(open("./models/vec_train.pickel", "rb"))

rfmodel = joblib.load('./models/rfmodel.pkl')

def home(request):
    return render(request, 'home.html')


def detect(request):
    if request.method == 'POST':
        seed_url = request.POST.get('url')
        article = Article(seed_url)
        article.download()
        article.parse()
        article.nlp()
        text = article.text
        author = article.authors
        summary = article.summary
        result = []
        for token in gensim.utils.simple_preprocess(text):
            if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 2 and token not in stop_words:
                result.append(token)
        text_join = [" ".join(result)]
    sentiment_string = ''.join(text_join)
    blob = TextBlob(sentiment_string)
    sent = blob.sentiment.polarity
    if sent > 0.7:
        polar = 'Positive'
    elif 0.3 < sent < 0.7:
        polar = 'Neutral'
    else:
        polar = 'Negative'
    new_vec = vec_train.transform(text_join)
    prediction = rfmodel.predict(new_vec)[0]
    if prediction >= 0.5:
        tof = 'Real'
    else:
        tof = 'Fake'

    context = {'tof':tof, 'author':author, 'summary': summary, 'polar':polar}

    return render(request, 'home.html', context)