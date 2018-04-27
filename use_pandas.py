import pandasas pd
df = pd.read_csv('salaries.csv')
df
df['Salary', 'Name']
df['Salary'].max()
df.describe()
myfilter = df['Salary'] > 60000
df[myfilter]
#df[df['Salary'] > 60000]
df.as_matrix()
