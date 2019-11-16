import tweepy
import pandas as pd     # To handle data
import numpy as np      # For number computing
import datetime as dt   





from credentials import *    # This will allow us to use the keys as variables






# Verify  the Printed values Access

print (CONSUMER_KEY)
print (CONSUMER_SECRET)

# Verify  the Printed values Access
print (ACCESS_TOKEN)
print (ACCESS_SECRET)


import tweepy
import time
    

auth=tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True)
api.update_status("Dummy Text here")
#time.sleep(6000)

from textblob import TextBlob
import re

def clean_tweet(tweet):
    '''
    Utility function to clean the text in a tweet by removing 
    links and special characters using regex.
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def analize_sentiment(tweet):
    '''
    Utility function to classify the polarity of a tweet
    using textblob.
    '''
    analysis = TextBlob(clean_tweet(tweet))
    if analysis.sentiment.polarity > 0:
        return 1
    elif analysis.sentiment.polarity == 0:
        return 0
    else:
        return -1
    


screen_name="@sagarcasm"

new_tweets = api.user_timeline(screen_name = screen_name,count=50, tweet_mode="extended")

for i in new_tweets:
    tweet = clean_tweet (i.full_text)
    
    print ("Tweet is:\n\n" + str(tweet) + "\n\n Polarity is: " + str(analize_sentiment(tweet)))




