##### 간단한 토큰화 ####
text = "Tokenization is the process of breaking down a text into smaller units called tokens."

tokens = text.split()
print(tokens)

##### 모듈을 이용한 토큰화 ############
# pip install nltk
import nltk
from nltk.tokenize import word_tokenize

# Word tokenization using NLTK
tokens = word_tokenize(text)

# Print the tokens
print(tokens)

# ##### 한글 토큰화 ##############
# # https://konlpy.org/ko/latest/index.html

from konlpy.tag import Okt, Kkma, Komoran, Hannanum

okt = Okt()
kkma = Kkma()
komoran = Komoran()
hannanum = Hannanum()

# text = '토큰화는 말뭉치를 토큰이라는 작은 단위로 분해하는 과정이다!'
# tokens = okt.morphs(text)
# print(tokens)

text = ['나랏말이중국과 달라 한자와 서로 통하지 아니하므로', 
    '우매한 백성들이 말하고 싶은 것이 있어도 마침내 제 뜻을 잘 표현하지 못하는 사람이 많다.',
    '내 이를 딱하게 여기어 새로 스물여덟 자를 만들었으니', 
    '사람들로 하여금 쉬 익히어 날마다 쓰는 데 편하게 할 뿐이다.']

for t in text:
    print('Okt:     ', okt.morphs(t))
    print('kkma:    ', kkma.morphs(t))
    print('komoran: ', komoran.morphs(t))
    print('hannanum:', hannanum.morphs(t), '\n')