import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import math
from scrape_reddit import topics_data

q = "How did George Bush steal an Election?"
q = "Is the Ku Ku Klux Klan Liberal?"

# Temporary questions to tokens
qt = nltk.word_tokenize(q)

reddit_questions = topics_data['title'].values
rq_list = []
q_tokens = []
for i in reddit_questions:
    q_tokens.append(nltk.word_tokenize(i))
    rq_list.append((i))

rq_list.append(q)

TfidfVec = TfidfVectorizer()
tfidf = TfidfVec.fit_transform(rq_list)

theta = []
for i in range(len(rq_list) - 1):
    val = cosine_similarity(tfidf[14], tfidf[i])

    theta.append(math.acos(val))

best_angle = min(theta)
print("Your question: " + q)
print("Answer: " + rq_list[theta.index(best_angle)])
print("Index: " + str(theta.index(best_angle)))

