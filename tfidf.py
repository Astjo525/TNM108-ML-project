import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import math
from pre_processing import pre_process

def minimum_cosine(query, data):
    query = pre_process(query)
    data = data.copy()
    data.append(query)

    #Transform all the answers and questions into tfidf vectors
    TfidfVec = TfidfVectorizer()
    tfidf = TfidfVec.fit_transform(data)

    #Store all the cosine angles in theta
    theta = []
    #Compute the cosine similarity between the query and the data.
    for i in range(len(data) - 1):
        val = cosine_similarity(tfidf[-1], tfidf[i])

        theta.append(math.acos(val))
    
    #Find the minimum angle and the index of that text from data and return it
    min_angle = min(theta)
    data_index = theta.index(min_angle)

    return min_angle, data_index

