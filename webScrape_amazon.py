# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 13:07:54 2018

@author: Tahrima 
"""

from lxml import html  
import requests
import pandas as pd

## Samsung Galaxy s9

reviews_df_SGS9 = pd.DataFrame()
#  https://www.amazon.com/Samsung-Galaxy-S9-Unlocked-Smartphone/product-reviews/B079H6RLKQ/ref=cm_cr_arp_d_viewopt_srt?ie=UTF8&reviewerType=all_reviews&pageNumber=1&sortBy=recent

for i in range(1,38):

    amazon_url = 'https://www.amazon.com/Samsung-Galaxy-S9-Unlocked-Smartphone/product-reviews/B079H6RLKQ/ref=cm_cr_arp_d_viewopt_srt?ie=UTF8&reviewerType=all_reviews&pageNumber='+str(i)+'&sortBy=recent'
    
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
                              
    headers = {'User-Agent': user_agent}
    page = requests.get(amazon_url, headers = headers)
    parser = html.fromstring(page.content)
    
    xpath_reviews = '//div[@data-hook="review"]'
    reviews = parser.xpath(xpath_reviews)   
    xpath_body    = './/span[@data-hook="review-body"]//text()'
    body = parser.xpath(xpath_body)
 
    for review in reviews:
        body    = review.xpath(xpath_body)
        review_dict = {'body': body}
        reviews_df_SGS9 = reviews_df_SGS9.append(review_dict, ignore_index=True)

reviews_df_SGS9

# append to csv 
reviews_df_SGS9.to_csv(r'C:\ttu\summer 18\dataMinning\p\tweets_s9.txt', header=None, index=None, sep=' ', mode='a') 


