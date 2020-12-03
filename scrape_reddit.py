import praw
import pandas as pd
import datetime as dt

from variables import *

#exec(open('scrape_reddit.py').read())

reddit = praw.Reddit(client_id=client_id, \
                     client_secret=client_secret, \
                     user_agent=user_agent, \
                     username=username, \
                     password=password)

numb_questions = 5

top_subreddit = reddit.subreddit('AskHistorians').top("month", limit=numb_questions)
topics_dict = { "title":[],
                "replies":[] }
excel_dict = { "title":[],
                "replies":[] }

# Go over each question
for submission in top_subreddit:
    # Add question to dictionary
    topics_dict["title"].append(submission.title)

    # Don't return "MoreComments"
    submission.comments.replace_more(limit=0)

    # Sort answers
    submission.comment_sort = 'best'

    # Go over answers
    answerList = []
    for comment in submission.comments[0:5]:

        # Check that comment hasn't been removed and isn't a comment by the moderator
        if (comment.author is not None and comment.distinguished is None):
            answerList.append(comment.body)
            excel_dict["title"].append(submission.title)
            excel_dict["replies"].append(comment.body)
            
    
    # Add answer list to dictionary
    topics_dict["replies"].append(answerList)

# Create data frame with questions/answers
topics_data = pd.DataFrame(topics_dict)

# Create Excel sheet with data
excel_data = pd.DataFrame(excel_dict)
excel_data.to_excel('history.xlsx', index=False)  