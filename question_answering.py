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

query = "How did George Bush steal an Election?"
#query = "How many eyes does a cat have?"
#query = "How many british monarch died in 2020?"
#query = "How do the states handle people convicted for marijuana after legalization?"

# Find similar question
[min_angle, data_index] = minimum_cosine(query, r_questions)

threshold = 1.3
# Check if angle is small enough to be a match
if(min_angle < threshold):
    answers_to_question = r_replies[data_index]
    # Find best answer to submitted query
    [min_angle_submitted_query, sub_index] = minimum_cosine(query, answers_to_question)

    # Find best answer to reddit question
    [min_angle_reddit_question, red_index] = minimum_cosine(r_questions[data_index], answers_to_question)
    
    print("Your question: " + query)
    print("Similar question: " + r_questions[data_index])
    print("Index: " + str(data_index))

    print("Submitted query answer: " + r_replies[data_index][sub_index][0:100])
    print("With answer index: " + str(sub_index))

    print("Reddit question answer: " + r_replies[data_index][red_index][0:100])
    print("With answer index: " + str(red_index))
else:
    print("Sorry, no matching question in the database")