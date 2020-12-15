import pandas as pd
from pre_processing import r_questions, r_replies
from tfidf import minimum_cosine

# Reload scripts
import tfidf
import pre_processing
import pre_proc_func
import importlib
importlib.reload(tfidf)
importlib.reload(pre_processing)
importlib.reload(pre_proc_func)

## RELOAD question_answering in command prompt
# import question_answering
# import importlib
# importlib.reload(question_answering)

#exec(open('question_answering.py').read())  

topics_data = pd.read_pickle('dataset.pkl')

query = "How did Ronald Reagan win the Election?"
query = "Did George Bush steal an election?"
query = "Why were women denied basic legal rights?"
#query = "How many british monarch died in 2020?"
#query = "How do the states handle people convicted for marijuana after legalization?"
#query = "Is it possible to invade Russia?"

# Find similar question
[min_angle, query_index] = minimum_cosine(query, r_questions)

threshold = 1.3
# Check if angle is small enough to be a match
if(min_angle < threshold):
    
    answers_to_question = r_replies[query_index]
    # Find best answer to submitted query
    [min_angle_submitted_query, sub_index] = minimum_cosine(query, answers_to_question)

    # Find best answer to reddit question
    [min_angle_reddit_question, red_index] = minimum_cosine(r_questions[query_index], answers_to_question)
    
    print("Your question: " + query)
    print("Similar question: " + topics_data['title'][query_index])
    print("Index: " + str(query_index))

    print("Submitted query answer: " + topics_data['replies'][query_index][sub_index])
    print("With answer index: " + str(sub_index))

    print("Reddit question answer: " + topics_data['replies'][query_index][red_index])
    print("With answer index: " + str(red_index))

    print("Reddit top answer: " + topics_data['replies'][query_index][0])
    print("With answer index: " + str(0))
else:
    print("Sorry, no matching question in the database")