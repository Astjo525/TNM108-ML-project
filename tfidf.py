import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import math
from pre_proc_func import pre_process

def minimum_cosine(query, data):
    query = pre_process(query)
    data = data.copy()
    data.append(query)

    TfidfVec = TfidfVectorizer()
    tfidf = TfidfVec.fit_transform(data)

    theta = []
    for i in range(len(data) - 1):
        val = cosine_similarity(tfidf[-1], tfidf[i])

        theta.append(math.acos(val))

    min_angle = min(theta)
    data_index = theta.index(min_angle)

    return min_angle, data_index

