import pandas as pd
import string
from gensim.parsing.preprocessing import remove_stopwords
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

#exec(open('pre_processing.py').read())

# history.xlsx = remove_stopwords(history.xlsx

topics_data = pd.read_excel (r'history.xlsx')

for i in topics_data['title']:
    i = remove_stopwords(i)
    i = i.lower()
    for c in string.punctuation:
        i= i.replace(c,"")
    
    print(i)

for i in topics_data['replies']:
    i = remove_stopwords(i)
    i = i.lower()
    for c in string.punctuation:
        i= i.replace(c,"")


# print(topics_data['title'])

