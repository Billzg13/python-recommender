from plotly.offline import iplot
import plotly.figure_factory as ff
from IPython.core.interactiveshell import InteractiveShell
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import re
import random
import plotly.graph_objs as go
#import chart_studio.plotly as py
import cufflinks
pd.options.display.max_columns = 30
InteractiveShell.ast_node_interactivity = 'all'
cufflinks.go_offline()
cufflinks.set_config_file(world_readable=True, theme='solar')

REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
STOPWORDS = set(stopwords.words('english'))

df = pd.read_csv('data/places_real.csv')
df = df.dropna()


def clean_text(text):
    """
        text: a string

        return: modified initial string
    """
    text = text.lower()  # lowercase text
    # replace REPLACE_BY_SPACE_RE symbols by space in text. substitute the matched string in REPLACE_BY_SPACE_RE with space.
    text = REPLACE_BY_SPACE_RE.sub(' ', text)
    # remove symbols which are in BAD_SYMBOLS_RE from text. substitute the matched string in BAD_SYMBOLS_RE with nothing.
    text = BAD_SYMBOLS_RE.sub('', text)
    # remove stopwors from text
    text = ' '.join(word for word in text.split() if word not in STOPWORDS)
    return text


df['word_count'] = df['description'].apply(lambda x: len(str(x).split()))
desc_lengths = list(df['word_count'])

df['description_clean'] = df['description'].apply(clean_text)

df.set_index('title', inplace=True)
tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3),
                     min_df=0, stop_words='english')
tfidf_matrix = tf.fit_transform(df['description_clean'])
cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)

indices = pd.Series(df.index)

print('ready to recommend!')


def predict(name, cosine_similarities=cosine_similarities):
    recommended_hotels = []

    # gettin the index of the hotel that matches the name
    idx = indices[indices == name].index[0]

    # creating a Series with the similarity scores in descending order
    score_series = pd.Series(
        cosine_similarities[idx]).sort_values(ascending=False)
    
    print('dads')
    print(score_series)
    
    # getting the indexes of the 10 most similar hotels except itself
    top_10_indexes = list(score_series.iloc[1:11].index)

    # populating the list with the names of the top 10 matching hotels
    for i in top_10_indexes:
        recommended_hotels.append(list(df.index)[i])

    return recommended_hotels
