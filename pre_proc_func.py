import pandas as pd
import string
import nltk
from gensim.parsing.preprocessing import remove_stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from scrape_reddit import topics_data,excel_data
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
#exec(open('pre_processing.py').read())

#For lemmatize, decides how the word should be bent according to if it is a adjective
def get_wordnet_pos(word):
    """Map POS tag to first character lemmatize() accepts"""
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)

def pre_process(i):
    i = remove_stopwords(i)
    i = i.lower()
    for c in string.punctuation:
        i= i.replace(c,"")
    
    i = ' '.join(x for x in i.split() if not x.startswith('http'))
    word_list = nltk.word_tokenize(i)
    lemmatized_output = ' '.join([wordnet_lemmatizer.lemmatize(w,get_wordnet_pos(w)) for w in word_list])
    return lemmatized_output