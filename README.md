# A Comparison of iPhone-8 & Samsung Galaxy-S8 by Sentiment Analysis from Product Review
## Introduction
The main idea of this project is to collect user sentiment about 2 very popular necessity products of our day to day lives and compare their user satisfaction level. The products I have chosen for this study is iPhone-8, the newest version of iPhone which is very popular in United states. However, some recent research show that iPhone popularity is declining day by day. The main reasons identified for this declining sale is the brand’s high price range and not being able to meet user satisfaction who are paying the price. 

On the other hand, the usability and feature range of Android phones are improving day by day. There are many products in the market that offer the same features as iPhone but with a much lower price. Thus, user expectations about the product quality and service is also lower for these products. The other product that will be compared in this project along with iPhone-8 is Samsung Galaxy S8, which is considered as having equal features, quality and service range as iPhone 8 but with a much lower price.

The objective of this study is to collect user comments and reviews straight from Twitter, Amazon, Gsmarena sites, which are very popular among people to express their sentiment about various products. This project will compare what are some of the positive and negative sides of these 2 products from user sentiment.

The business problem this project aims to identify is such: what is the user sentiment who are using these two products in their daily life. Also, what are some of the meanings behind the reviews and what impact those latent meanings might have in the future of these products. Both the brands producing these phones can learn from this analysis the most important aspects that users love and hate about the phones. Thus this project can help the companies improve their products as well as sale and user satisfaction by gaining knowledge from the user sentiment available in the internet. 

## Data Source
The data for this project has been collected from various sources. All the reviews of iPhone-8 have been collected from Twitter API. Twitter offers an API by which anyone can collect tweets with API keys. The collection of the tweets for iPhone-8 was filtered by the string “iPhone 8” and only the tweets written in English were collected. The tweets were collected in the file “8.txt” for a period of 10-12 hours and the initial file size of tweets was 10MB. Later only the texts and country information of the tweets were saved to another file for further analysis. This part of the project is done in Python using popular Python libraries as needed. 
In the next page, a plot is shown on the origin of the tweets. The countries from which people tweeted most about iPhone-8 are visualized. This information was also gathered from the ‘country’ attribute collected through Twitter API. 


