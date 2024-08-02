import pandas as pd

data_path = "C:/Users/elesi/Downloads/감성대화말뭉치(최종데이터)_Training.xlsx"
use_cols = ['연령','성별','상황키워드','신체질환','감정_대분류','감정_소분류','사람문장1']
data = pd.read_excel(data_path, sheet_name='Sheet1', usecols=use_cols, dtype_backend='pyarrow')

cols = ['연령','성별','신체질환','감정_대분류','감정_소분류','사람문장1']
print(data[cols])

# data_pivot = pd.pivot_table(data, index='연령', columns='성별', values='사람문장1', aggfunc='count')
data_pivot = pd.pivot_table(data, index=['감정_대분류','감정_소분류'], values='사람문장1', aggfunc='count')
print(data_pivot)