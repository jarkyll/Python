#!/usr/bin/env python

#python api

import praw
#python reddit api wrapper

r = praw.Reddit(user_agent = "my_cool_app")
# object is above




types = ["hot", "new", "rising", "controversial", "top", "gilded", "wiki"]

subreddit ="askreddit"
#= input("What subreddit do you want to go to?: ")
post_type ="wiki"
#= input("\nWhich type of post do you want to see in " + subreddit + " or do you want to see the wiki of the subreddit?")
#num_posts = int( input("How many of the hot posts of " + subreddit + " do you want to view?: "))



while subreddit is None:
    subreddit = input("Please put a valid subreddit name: ")
    
while post_type is None:
    post_type = input("Please put a valid type of subreddit: ")

if post_type == "wiki":
    wikiObjects = str( r.get_wiki_pages(subreddit))
    for x in wikiObjects:
        print(x, end='')

    

    
#submission = r.get_subreddit(subreddit).get_hot(limit=num_posts)

#for x in submission:
#    print( str(x))

