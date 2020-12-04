import pandas as pd
from django.shortcuts import render
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder

tokenizer = RegexpTokenizer(r'\w+')
ps = PorterStemmer()
le = LabelEncoder()
model = MultinomialNB()
cv = CountVectorizer()

stopwords = ['to',
             'if',
             'which',
             'while',
             'in',
             'few',
             'their',
             'ourselves',
             'him',
             "isn't",
             "mightn't",
             "wouldn't",
             'our',
             'further',
             "doesn't",
             'after',
             'nor',
             'not',
             'so',
             'the',
             't',
             'what',
             'any',
             'more',
             "aren't",
             "didn't",
             'because',
             'has',
             "hadn't",
             'from',
             'have',
             'own',
             'how',
             'ain',
             'were',
             "mustn't",
             'they',
             'themselves',
             'we',
             'just',
             'of',
             'against',
             'won',
             'ours',
             'this',
             "shouldn't",
             'your',
             'then',
             'ma',
             'had',
             'myself',
             'each',
             'he',
             'only',
             "you'd",
             'these',
             "you've",
             'she',
             'haven',
             'here',
             'such',
             'do',
             'once',
             'o',
             'hasn',
             'you',
             'was',
             "wasn't",
             'some',
             's',
             'are',
             'is',
             "you're",
             'up',
             "hasn't",
             'can',
             'as',
             'y',
             'there',
             'same',
             'herself',
             'and',
             'all',
             "couldn't",
             'under',
             'with',
             'out',
             'those',
             'been',
             'before',
             'into',
             "you'll",
             'its',
             'who',
             'again',
             "should've",
             'but',
             'above',
             'it',
             'now',
             'most',
             'i',
             'down',
             'off',
             "that'll",
             'why',
             'doesn',
             'shouldn',
             'did',
             'between',
             'on',
             "weren't",
             'by',
             'below',
             'hadn',
             'isn',
             'didn',
             'through',
             'shan',
             "needn't",
             'needn',
             'them',
             'that',
             'weren',
             'very',
             'don',
             'for',
             'be',
             'aren',
             'her',
             're',
             'itself',
             'whom',
             'until',
             "it's",
             'doing',
             'no',
             'yours',
             've',
             "she's",
             'yourself',
             'having',
             'at',
             "haven't",
             'other',
             'his',
             'does',
             'will',
             'mightn',
             'yourselves',
             'both',
             'being',
             'wouldn',
             'theirs',
             'a',
             'himself',
             'd',
             'wasn',
             "won't",
             "shan't",
             'my',
             'about',
             'during',
             'than',
             'an',
             'hers',
             "don't",
             'over',
             'or',
             'me',
             'll',
             'am',
             'where',
             'couldn',
             'should',
             'too',
             'm',
             'mustn',
             'when']

def index(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        check2(content)
    return render(request, 'index.html')


def remove_stopwords(text, stopwords):
    useful = [w for w in text if w not in stopwords]
    return useful


def getDoc(document):
    d = []
    for doc in document:
        d.append(getStem(doc))
    return d


def getStem(review):
    review = review.lower()
    tokens = tokenizer.tokenize(review)
    removed_stopwords = [w for w in tokens if w not in stopwords]
    correct = []
    for ch in removed_stopwords:
        if ('\u0600' <= ch <= '\u06FF' or
                '\u0750' <= ch <= '\u077F' or
                '\u08A0' <= ch <= '\u08FF' or
                '\uFB50' <= ch <= '\uFDFF' or
                '\uFE70' <= ch <= '\uFEFF' or
                '\U00010E60' <= ch <= '\U00010E7F'):
            pass
        else:
            correct.append(ch)
    stemmed_words = [ps.stem(token) for token in correct]
    clean_review = ' '.join(stemmed_words)
    return clean_review


def check1(content):
    df = pd.read_csv('test.csv')
    data = df.to_numpy()
    Y = data[:, 2]
    X = data[:, 1]
    y = []
    for i in Y:
        if i == 1:
            y.append("No")
        else:
            y.append("Yes")

    stemmed_doc = getDoc(X)
    cv = CountVectorizer()
    vc = cv.fit_transform(stemmed_doc)
    X = vc.toarray()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(cv.transform(getDoc([content])))
    print(y_pred)


def check2(content):
    df = pd.read_csv('test.csv')
    data = df.to_numpy()
    y = data[:, 1]
    X = data[:, 0]
    stemmed_doc = getDoc(X)
    cv = CountVectorizer()
    vc = cv.fit_transform(stemmed_doc)
    X = vc.toarray()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(cv.transform(getDoc([content])))
    print(y_pred)
