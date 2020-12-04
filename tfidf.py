import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import math
from pre_processing import r_questions, r_replies
from pre_proc_func import pre_process
from scrape_reddit import topics_data

## RELOAD SCRIPT
import importlib
import pre_proc_func
import pre_processing
importlib.reload(pre_proc_func)
importlib.reload(pre_processing)
## END RELOAD SCRIPT

## RELOAD tfidf in command prompt
# import tfidf
# import importlib
# importlib.reload(tfidf)

query = "How did George Bush steal an Election?"
query = "How many eyes does a cat have?"
query = "How many british monarch died in 2020?"
query = "How do the states handle people convicted for marijuana after legalization?"

query = pre_process(query)

r_questions.append(query)

print(r_questions)

TfidfVec = TfidfVectorizer()
tfidf = TfidfVec.fit_transform(r_questions)

theta = []
for i in range(len(r_questions) - 1):
    val = cosine_similarity(tfidf[-1], tfidf[i])

    theta.append(math.acos(val))

best_angle = min(theta)

threshold = 1.3
if(best_angle < threshold):
    print("Your question: " + query)
    print("Similar question: " + r_questions[theta.index(best_angle)])
    print("Index: " + str(theta.index(best_angle)))
else:
    print("Sorry, no matching question in the database")

