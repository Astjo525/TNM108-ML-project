import pandas as pd
import string
import nltk
from gensim.parsing.preprocessing import remove_stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from scrape_reddit import topics_data,excel_data
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
from pre_proc_func import pre_process
#exec(open('pre_processing.py').read())

## RELOAD SCRIPT
import importlib
import pre_proc_func
importlib.reload(pre_proc_func)
## END RELOAD SCRIPT


#For lemmatize, decides how the word should be bent according to if it is a adjective
def get_wordnet_pos(word):
    """Map POS tag to first character lemmatize() accepts"""
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)

# Collect the data
reddit_questions = excel_data['title']
reddit_replies = excel_data['replies']

# Create lists for questions and replies
r_questions = []
r_replies = []

# Remove stopwords, punctuation, lowercase, remove links and lemmantize for the questions 
for i in reddit_questions:
    lemmatized_output = pre_process(i)
    # i = remove_stopwords(i)
    # i = i.lower()
    # for c in string.punctuation:
    #     i= i.replace(c,"")

    # i = ' '.join(x for x in i.split() if not x.startswith('http'))
    # word_list = nltk.word_tokenize(i)
    # lemmatized_output = ' '.join([wordnet_lemmatizer.lemmatize(w,get_wordnet_pos(w)) for w in word_list])
    r_questions.append(lemmatized_output)

# Remove stopwords, punctuation, lowercase, remove links and lemmantize for the replies
for i in reddit_replies:
    lemmatized_output = pre_process(i)
    # i = remove_stopwords(i)
    # i = i.lower()
    # for c in string.punctuation:
    #     i= i.replace(c,"")
    
    # i = ' '.join(x for x in i.split() if not x.startswith('http'))
    # word_list = nltk.word_tokenize(i)
    # lemmatized_output = ' '.join([wordnet_lemmatizer.lemmatize(w,get_wordnet_pos(w)) for w in word_list])
    r_replies.append(lemmatized_output)




