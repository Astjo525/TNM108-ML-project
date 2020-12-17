import praw
import pandas as pd
import datetime as dt

from summa.summarizer import summarize

from variables import *

#Using praw to scrape Reddit, with our app
reddit = praw.Reddit(client_id=client_id, \
                     client_secret=client_secret, \
                     user_agent=user_agent, \
                     username=username, \
                     password=password)

#Scrape the 100 first questions 
numb_questions = 100

#Scrape the subreddit AskHistorians with the 100 top questions of all time.
top_subreddit = reddit.subreddit('AskHistorians').top("all", limit=numb_questions)

topics_dict = { "title":[],
                "replies":[] }

# Go over each question
for submission in top_subreddit:

    # Don't return "MoreComments"
    submission.comments.replace_more(limit=0)

    # Sort answers
    submission.comment_sort = 'best'

    # Go over answers
    answerList = []
    commentIndex = 0
    for comment in submission.comments:

        #Summarize comment in 150 words
        summarizedAnswer = summarize(comment.body, words = 150)

        # Check that comment hasn't been removed and isn't a comment by the moderator
        if (comment.author is not None and comment.distinguished is None and len(summarizedAnswer) > 0):
            answerList.append(summarizedAnswer)

            #Check if question has five answers
            if(len(answerList) == 5):
                # Add question to dictionary
                topics_dict["title"].append(submission.title)

                # Add answer list to dictionary
                topics_dict["replies"].append(answerList)
                break 
            

# Create DataFrame with questions/answers
topics_data = pd.DataFrame(topics_dict)

# Save DataFrame to .pkl file
topics_data.to_pickle('dataset.pkl')

