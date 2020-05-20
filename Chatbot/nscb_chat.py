import pandas as pd
import re
pd.set_option('display.max_colwidth', 200)

df = pd.read_csv(r'notsocleverbot.csv', encoding='latin-1')
df.head()

# Extract only the required info
convo = df.iloc[:,1]
convo

# Use regular expression to from question response pairs
clist = []
def qa_pairs(x):
    cpairs = re.findall(": (.*?)(?:$|\\n)", x)
    clist.extend(list(zip(cpairs, cpairs[1:])))
convo.map(qa_pairs);
convo_frame = pd.Series(dict(clist)).to_frame().reset_index()
convo_frame.columns = ['q', 'a']
#convo_frame

# Transform the training data to Tf-IDF form
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
vectorizer = TfidfVectorizer(ngram_range=(1,3))
vec = vectorizer.fit_transform(convo_frame['q'])

# Define a function to find the most matching response to an input question
def get_response(q):
    my_q = vectorizer.transform([q])
    cs = cosine_similarity(my_q, vec)
    rs = pd.Series(cs[0]).sort_values(ascending=0)
    rsi = rs.index[0]
    return convo_frame.iloc[rsi]['a']

# Testing the model
print(get_response('Yes, I am clearly more clever than you will ever be!'))

query = input("Enter a question!\n")
while(query != 'quit'):
	print(get_response(query))
	query = input("")
