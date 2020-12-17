import pandas as pd
import pickle

from pre_processing import pre_process

topics_data = pd.read_pickle('dataset.pkl')

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

# Save processed data to file
with open('processed_data.pkl', 'wb') as filehandle:
    pickle.dump(r_questions, filehandle)
    pickle.dump(r_replies, filehandle)



