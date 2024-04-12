import numpy as np
import pandas as pd
from konlpy.tag import Okt
from gensim.models import Word2Vec, FastText

# tokenization
def tokenization():

    data = pd.read_table("ratings_train.txt")[:10]
    
    tokenizer = Okt()

    def process_tokens(doc):
        results = tokenizer.pos(doc)

        tokens = []
        for r in results:
            token, pos = r
            if pos == 'Noun' or pos == 'Adjective':
                tokens.append(token)
        return tokens    

    data['tokens'] = data['document'].apply(lambda x: process_tokens(x))
    return data

data = tokenization()

tokenized_data = data['tokens']

# train word2vec model
wvmodel = Word2Vec(
    sentences = tokenized_data,
    vector_size = 5,
    min_count = 1,
    window = 5,
    sg = 1
)

print(tokenized_data)

embeddings = []
for tokens in tokenized_data:
    # print(tokens) 
    tokens_vectors = []
    for token in tokens:
        vectors = wvmodel.wv[token]
        tokens_vectors.append(vectors)
    
    # print(tokens_vectors)
    vectors_array = np.array(tokens_vectors)
    # print(vectors_array, vectors_array.shape)
    
    embedding = np.mean(vectors_array, axis=0)
    # print(embedding, embedding.shape)
    
    embeddings.append(embedding)

embeddings_array = np.array(embeddings)
print(embeddings_array, embeddings_array.shape)

data['embedding'] = embeddings
print(data.drop('tokens', axis=1))