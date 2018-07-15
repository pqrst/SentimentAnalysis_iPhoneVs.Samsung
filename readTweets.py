# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 13:36:24 2018

@author: oishe_000
"""

import json
import pandas as pd
import matplotlib.pyplot as plt
import re
import numpy as np

tweets_data_path = 'C:/ttu/summer 18/dataMinning/p/s9.txt'

# saving the tweets 
tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue
    
# printing the length of tweets_data
print(len(tweets_data)) 

# structuring the tweets in a dataframe 
tweets = pd.DataFrame()

# saving tweet, its langugae and country in the dataframe
tweets['text'] = list(map(lambda tweet: tweet['text'], tweets_data))
tweets['country'] = list(map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data))

tweets_by_country = tweets['country'].value_counts()

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Countries', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')

# save data into txt file 
tweets['text'].to_csv(r'C:\ttu\summer 18\dataMinning\p\tweets_8.txt', header=None, index=None, sep=' ', mode='a')






