# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 14:37:41 2018

@author: tahrima
"""


from lxml import html  
import requests
import pandas as pd

## Samsung Galaxy s9

gsmreviews_df_SGS9 = pd.DataFrame()
#  https://www.gsmarena.com/samsung_galaxy_s9-reviews-8966p2.php

for i in range(1,40):

    gsm_url = 'https://www.gsmarena.com/samsung_galaxy_s9-reviews-8966p'+str(i)+'.php'
 #   gsm_url = 'https://www.gsmarena.com/samsung_galaxy_s9-reviews-8966p40.php'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
                              
    headers = {'User-Agent': user_agent}
    page = requests.get(gsm_url, headers = headers)
    parser = html.fromstring(page.content)

#    xpath_reviews = '//div[@class="user-thread"]'
#    reviews = parser.xpath(xpath_reviews)   

    xpath_msg  = './/p[@class="uopin"]//text()'
    msg = parser.xpath(xpath_msg)
    
    review_dict = {'body': msg}
    gsmreviews_df_SGS9 = gsmreviews_df_SGS9.append(review_dict, ignore_index=True)
    
gsmreviews_df_SGS9

# append to csv 
gsmreviews_df_SGS9.to_csv(r'C:\ttu\summer 18\dataMinning\p\tweets_s9.txt', header=None, index=None, sep=' ', mode='a') 
