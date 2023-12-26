# twitter Bot.

import tweepy

# A file to store all the keys and tokens.
from config import * 


# # auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# # auth.set_access_token(access_token, access_token_secret)


# V1 twitter API Authentication.

auth = tweepy.OAuth1UserHandler(api_key, api_key_secret) 
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# V2 twitter API Authentication.
client = tweepy.Client(
    bearer_token,
    api_key, 
    api_key_secret, 
    access_token, 
    access_token_secret)

api = tweepy.API(auth)

print('Authentication Successful !')


# Create a new tweet. (Working)
client.create_tweet(text = r"Hello this is the 2'nd tweet from my Twitter Bot {Sachin}")
