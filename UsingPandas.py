import pandas as pd
df = pd.read_csv('data.csv')
df
df = pd.read_csv('data.csv', index_col='Col')
df
df.dtypes
df.head()
df.tail()
df.columns
df.describe()
df['Total']
df[2:6]
df[df.Rank == 1]
df.loc['val']
