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

subreddit = reddit.subreddit('AskHistorians/wiki/faq/europe')
subreddit = reddit.subreddit('AskHistorians')

top_subreddit = subreddit.top("month", limit=5)

# for submission in top_subreddit:
#     submission.comments.replace_more(limit=None)
#     for comment in submission.comments.list():
#         print(comment.body)

# for submission in subreddit.top(limit=2):
#     print(submission.title, submission.id)

topics_dict = { "title":[],
                "replies":[] }
            # "score":[], 
            # "id":[], "url":[], 
            # "comms_num": [], 
            # "created": [], 
            # "body":[],
            # "replies":[]}

for submission in top_subreddit:
    submission.comments.replace_more(limit=0)
    #topics_dict["title"].append(submission.title)
    #topics_dict["replies"].append(submission.comments[:5])
    for comment in submission.comments[2:5]:
        topics_dict["title"].append(submission.title)
        topics_dict["replies"].append(comment.body)


topics_data = pd.DataFrame(topics_dict)

topics_data.to_csv('history.csv', index=False)
topics_data.to_excel('history.xlsx', index=False)  