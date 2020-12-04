import pandas as pd

from django.shortcuts import render
from sklearn.model_selection import train_test_split

from services.globals import *


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
    removed_stopwords = [w for w in tokens if w not in stop_words]
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
    df = pd.read_csv('df.csv')
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
