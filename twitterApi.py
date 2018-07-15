# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 12:39:26 2018

@author: oishe_000
"""

import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
 
# Twitter api information
consumer_key = '...'
consumer_secret = '...'
access_token = '...'
access_token_secret = '...'
 

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authentification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    stream.filter(track=['Samsung Galaxy S9'], languages=['en'])
    
    
    
    
    
    
    
    
    
    
    
    