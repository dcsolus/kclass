import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_table('ratings_train.txt')

df = pd.pivot_table(dataset, index='label', values='document', aggfunc='count').reset_index()
print(df)
df.plot(kind='bar', x='label', y='document')
plt.show()