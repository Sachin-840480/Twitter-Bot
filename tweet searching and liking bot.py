# twitter bot 1 and 2.

import tweepy
import time

from config import *

# Setting and Authenticating to Twitter API.

auth = tweepy.OAuth1UserHandler(api_key, api_key_secret) 
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
print('Authentication Successful !')


#this part searches tweets with a matching 'string' and like the tweet.

search_string = 'python'
numbers_of_tweet = 2

for tweet in tweepy.Cursor(api.search_tweets, search_string).items(numbers_of_tweet):
    try:
        tweet.favorite()
        print('I liked the tweet')
    except tweepy.TweepyException as e:
        print(e.response)
    except StopIteration:
        break


#we can use it to like our own tweets.

search_string = 'Sachin Kumar'
numbers_of_tweet = 5

for tweet in tweepy.Cursor(api.search_tweets, search_string).items(numbers_of_tweet):
    try:
        tweet.favorite()
        print('I liked the tweet')
    except tweepy.TweepyException as e:
        print(e.response)
    except StopIteration:
        break


#retweet a tweet.
tweet.retweet() 
