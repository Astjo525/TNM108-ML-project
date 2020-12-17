import pandas as pd
import string
import nltk
from gensim.parsing.preprocessing import remove_stopwords 
from scrape_reddit import topics_data,excel_data
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
#exec(open('pre_processing.py').read())

#For lemmatize
def get_wordnet_pos(word):
    #tag is the POS tag that the lemmantize() accepts
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    #Return the tag if it is in tag_dict else the POS tag noun
    return tag_dict.get(tag, wordnet.NOUN)

def pre_process(i):
    i = remove_stopwords(i) 
    i = i.lower()
    #Replace each punctuation with a empty string
    for c in string.punctuation:  
        i= i.replace(c,"")
    #Remove the links from the sentences
    i = ' '.join(x for x in i.split() if not x.startswith('http'))
    #Split the string into the words and use lemmatize to stem the word
    word_list = nltk.word_tokenize(i)
    lemmatized_output = ' '.join([wordnet_lemmatizer.lemmatize(w,get_wordnet_pos(w)) for w in word_list])
    return lemmatized_output