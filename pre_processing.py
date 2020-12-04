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
from scrape_reddit import topics_data
#exec(open('pre_processing.py').read())

# Collect the data
reddit_questions = topics_data['title']
reddit_replies = topics_data['replies']

# Create lists for questions and replies
r_questions = []
r_replies = []

# Remove stopwords, punctuation, lowercase, remove links and lemmantize for the questions 
for i in reddit_questions:
    lemmatized_output = pre_process(i)
    r_questions.append(lemmatized_output)

# Remove stopwords, punctuation, lowercase, remove links and lemmantize for the replies
for replies in reddit_replies:
    answer_list = []
    for i in replies:
        lemmatized_output = pre_process(i)
        answer_list.append(lemmatized_output)
    r_replies.append(answer_list)




