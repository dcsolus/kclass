##### 영화리뷰 데이터 다운로드 ####
# 네이버 영화 리뷰 데이터 https://github.com/e9t/nsmc

import pandas as pd

data = pd.read_table("ratings_train.txt")[:10]

# tokenization
from konlpy.tag import Okt

tokenizer = Okt()

# step1: 토큰화 예시
# for idx, row in data.iterrows():
#     doc = row['document']
#     print(doc)
    
#     results = tokenizer.pos(doc)
    
#     tokens = []
#     for r in results:
#         token, pos = r
#         if pos == 'Noun' or pos == 'Adjective':
#             tokens.append(token)
    
#     print(tokens)
    
#     break

# step2: 함수 만들어 토큰화

def process_tokens(doc):
    results = tokenizer.pos(doc)

    tokens = []
    for r in results:
        token, pos = r
        if pos == 'Noun' or pos == 'Adjective':
            tokens.append(token)
    return tokens    

data['tokens'] = data['document'].apply(lambda x: process_tokens(x))
data = data.drop('document', axis=1)
# print(data)


##### 임베딩 #####
# library : gensim
from gensim.models import Word2Vec, FastText

tokenized_data = data['tokens']

# train word2vec model
wvmodel = Word2Vec(
    sentences = tokenized_data,
    vector_size = 2,
    min_count = 1,
    window = 5,
    sg = 1
)

# FastText 임베딩
ftmodel = FastText(
    sentences=tokenized_data,
    vector_size=10,
    min_count=1,
    window=5,
    sg=1
)


# 가장 유사한 벡터 찾기
for tokens in tokenized_data:
    print(tokens)
    
    for token in tokens:
        print('word2vec:', token, wvmodel.wv[token], wvmodel.wv.most_similar(token, topn=3))
        print('fasttext:', token, ftmodel.wv[token], ftmodel.wv.most_similar(token, topn=3))
        print('\n')
        
    break


