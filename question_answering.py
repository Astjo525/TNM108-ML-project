import pandas as pd
import pickle

from tfidf import minimum_cosine

# Reload scripts
import tfidf
import pre_processing
import data_processing
import importlib
importlib.reload(tfidf)
importlib.reload(pre_processing)
importlib.reload(data_processing)

# Run the code with this command
#exec(open('question_answering.py').read())  

topics_data = pd.read_pickle('dataset.pkl')

with open('processed_data.pkl', 'rb') as filehandle:
    r_questions = pickle.load(filehandle)
    r_replies = pickle.load(filehandle)

queries = ["How did Ronald Reagan win the Election?",
            "Did George Bush steal an election?",
            "Why were women denied basic legal rights?",
            "How many british monarch died in 2020?",
            "How do the states handle people convicted for marijuana after legalization?",
            "Is it possible to invade Russia?"
            "Was George Floyd murdered?",
            "Why is tear gas not used in warfare, but on civilians?",
            "Why is America, a country developed by immigrants, anti-immigration?"]

# Decide which of the queries should be submitted
query = queries[0]

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