# Library for Twitter API
import tweepy
from tweepy import OAuthHandler
 
# Auth to Twitter
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

# Onward then...

# Timeline items
for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    process_or_store(status._json) 

# # Followers
# for friend in tweepy.Cursor(api.friends).items():
#     process_or_store(friend._json)

# # List of all our tweets
# for tweet in tweepy.Cursor(api.user_timeline).items():
#     process_or_store(tweet._json)

def process_or_store(tweet):
    print(json.dumps(tweet))