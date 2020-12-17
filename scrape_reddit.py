import praw
import pandas as pd
import datetime as dt

from summa.summarizer import summarize

from variables import *

#exec(open('scrape_reddit.py').read())

#Using praw to scrape Reddit, with our app
reddit = praw.Reddit(client_id=client_id, \
                     client_secret=client_secret, \
                     user_agent=user_agent, \
                     username=username, \
                     password=password)

#scrape the 100 first questions 
numb_questions = 100

#Scrape the subreddit AskHistorians with the 100 top questions of all time.
top_subreddit = reddit.subreddit('AskHistorians').top("all", limit=numb_questions)
topics_dict = { "title":[],
                "replies":[] }
excel_dict = { "title":[],
                "replies":[] }
answer_dict = {"answers": []}

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

        summarizedAnswer = summarize(comment.body, words = 150)

        # Check that comment hasn't been removed and isn't a comment by the moderator
        if (comment.author is not None and comment.distinguished is None and len(summarizedAnswer) > 0):
            answerList.append(summarizedAnswer)

            if(len(answerList) == 5):
                answer_dict["answers"].append([summarizedAnswer])
                excel_dict["title"].append(submission.title)
                excel_dict["replies"].append(summarizedAnswer)

                # Add question to dictionary
                topics_dict["title"].append(submission.title)

                # Add answer list to dictionary
                topics_dict["replies"].append(answerList)
                break 
            

# Create data frame with questions/answers
topics_data = pd.DataFrame(topics_dict)

topics_data.to_pickle('dataset.pkl')

# Create Excel sheet with data
excel_data = pd.DataFrame(excel_dict)
excel_data.to_excel('history.xlsx', index=True)  

