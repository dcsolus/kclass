from math import log
import pandas as pd
import numpy as np

docs = [
	"배가 부르다",
	"배의 가격이 비싸다",
	"진짜 사과가 진짜 좋다",
	"아침엔 사과가 좋다"
]

vocab = list(set(w for doc in docs for w in doc.split()))
vocab.sort()
print('vocabulary:', vocab)

N = len(docs)

def tf(t, d):
    return d.count(t) / len(d)

def idf(t):
    df = 0
    for doc in docs:
        df += t in doc
    return log(N/(df + 1)) # 분모가 0이 되는 것을 방지

def tfidf(t, d):
    return tf(t,d) * idf(t)

tf_results = []
for i, d in enumerate(docs):
    result = []
    for j, t in enumerate(vocab):
        result.append(tf(t,d))
    tf_results.append(result)
    
tf_ = pd.DataFrame(tf_results, columns=vocab)
tf_array = tf_.values
print(tf_)
print(tf_array, tf_array.shape)


idf_results = []
for t in vocab:
    idf_results.append(idf(t))
    
idf_ = pd.DataFrame(idf_results, index = vocab, columns = ['idf'])
idf_ = idf_.reset_index()
idf_.rename(columns={'index':'vocab'}, inplace=True)
print(idf_)

tfidf_results = []
for d in docs:
    result = []
    for t in vocab:
        result.append(tfidf(t,d))
    tfidf_results.append(result)
    
tfidf_ = pd.DataFrame(tfidf_results, columns=vocab)
tfidf_array = tfidf_.values
print(tfidf_)
print(tfidf_array, tfidf_array.shape)