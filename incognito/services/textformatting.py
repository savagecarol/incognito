from services.globals import *


def remove_stopwords(text, stopwords):
    useful = [w for w in text if w not in stopwords]
    return useful


def formatting(document):
    document = document.lower()
    words = tokenizer.tokenize(document)
    useful_words = remove_stopwords(words, stopwords)
    stemmed_words = [ps.stem(token) for token in useful_words]
    clean_doc = ' '.join(stemmed_words)
    print(clean_doc)