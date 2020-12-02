import pandas as pd
import string
import nltk
from gensim.parsing.preprocessing import remove_stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from scrape_reddit import topics_data
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
#exec(open('pre_processing.py').read())

#For lemmatize, decides how the word should be bent
def get_wordnet_pos(word):
    """Map POS tag to first character lemmatize() accepts"""
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)


# Collect the data
reddit_questions = topics_data['title'].values
reddit_replies = topics_data['replies'].values

# Create lists for questions and replies
r_questions = []
r_replies = []

# Remove stopwords, punctuation, lowercase and lemmantize for the questions 
for i in reddit_questions:
    i = remove_stopwords(i)
    i = i.lower()
    for c in string.punctuation:
        i= i.replace(c,"")

    word_list = nltk.word_tokenize(i)
    lemmatized_output = ' '.join([wordnet_lemmatizer.lemmatize(w,get_wordnet_pos(w)) for w in word_list])
    r_questions.append(lemmatized_output)

# Remove stopwords, punctuation, lowercase and lemmantize for the replies
for i in reddit_replies:
    i = remove_stopwords(i)
    i = i.lower()
    for c in string.punctuation:
        i= i.replace(c,"")
    
    word_list = nltk.word_tokenize(i)
    lemmatized_output = ' '.join([wordnet_lemmatizer.lemmatize(w,get_wordnet_pos(w)) for w in word_list])
    r_replies.append(lemmatized_output)


