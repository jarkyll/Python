#!usr/bin/env python

#reddit bot 1

import praw

user_agent = ("Python b0t 0.1")

r = praw.Reddit(user_agent = user_agent)

subreddit = r.get_subreddit("learnpython")


for submission in subreddit.get_hot(limit = 5):
    #gets each submission from the get_hot function in this case 5
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("-"*150,"\n")
