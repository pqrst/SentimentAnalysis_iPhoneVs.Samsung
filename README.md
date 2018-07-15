# A Comparison of iPhone-8 & Samsung Galaxy-S8 by Sentiment Analysis from Product Review
## Introduction
The main idea of this project is to collect user sentiment about 2 very popular necessity products of our day to day lives and compare their user satisfaction level. The products I have chosen for this study is iPhone-8, the newest version of iPhone which is very popular in United states. However, some recent research show that iPhone popularity is declining day by day. The main reasons identified for this declining sale is the brand’s high price range and not being able to meet user satisfaction who are paying the price. 

On the other hand, the usability and feature range of Android phones are improving day by day. There are many products in the market that offer the same features as iPhone but with a much lower price. Thus, user expectations about the product quality and service is also lower for these products. The other product that will be compared in this project along with iPhone-8 is Samsung Galaxy S8, which is considered as having equal features, quality and service range as iPhone 8 but with a much lower price.

The objective of this study is to collect user comments and reviews straight from Twitter, Amazon, Gsmarena sites, which are very popular among people to express their sentiment about various products. This project will compare what are some of the positive and negative sides of these 2 products from user sentiment.

The business problem this project aims to identify is such: what is the user sentiment who are using these two products in their daily life. Also, what are some of the meanings behind the reviews and what impact those latent meanings might have in the future of these products. Both the brands producing these phones can learn from this analysis the most important aspects that users love and hate about the phones. Thus this project can help the companies improve their products as well as sale and user satisfaction by gaining knowledge from the user sentiment available in the internet. 

## Data Source
The data for this project has been collected from various sources. All the reviews of iPhone-8 have been collected from Twitter API. Twitter offers an API by which anyone can collect tweets with API keys. The collection of the tweets for iPhone-8 was filtered by the string “iPhone 8” and only the tweets written in English were collected. The tweets were collected in the file “8.txt” for a period of 10-12 hours and the initial file size of tweets was 10MB. Later only the texts and country information of the tweets were saved to another file for further analysis. This part of the project is done in Python using popular Python libraries as needed. 
In the next page, a plot is shown on the origin of the tweets. The countries from which people tweeted most about iPhone-8 are visualized. This information was also gathered from the ‘country’ attribute collected through Twitter API. 

![8_country](https://user-images.githubusercontent.com/5343403/42731294-9e7f47b8-87cf-11e8-8393-b0a31420528e.png)
The above plot shows the countries of the reviewers whose tweets about iPhone-8 was collected. The plot confirms the notion that iPhones are most popular in United States. 

The next dataset was collected about Samsung Galaxy S8 phones through the Twitter API. Unfortunately, finding English tweets about the Samsung Galaxy S8 was not as smooth as the collecting tweets about iPhone. One possible reason behind the situation can be Twitter is more popular in the United States where iPhones are very popular. 

After a span of about 24 hours the number of tweets collected in “s9.txt” file was very small with a size of only 2MB. Thus, more reviews of users were collected by web scraping. User reviews from Amazon (around 370 product reviews) and Gsmarena (around 140 product reviews) were collected through this process.  All the tweets and reviews were then combined into a csv file (tweets_s9.csv) for further analysis with sentiment analysis. The web scraping and tweet collection process part of the project is done in Python using popular Python libraries as needed. 

![s9_country](https://user-images.githubusercontent.com/5343403/42731310-0d4d4424-87d0-11e8-9c40-8cb143972555.png)
The above plot generated from tweets shows that unlike iPhone 8, tweets about Galaxy S8 are low from United States. Rather this graph tells us that Samsung Galaxy phones are more popular in European countries. However, since tweets written only in English are collected for this study, it is evident that this plot is not showing the full scenario about the popularity of Samsung Galaxy S8 phone in Europe. Since the first language of most of the European countries is not English. 

## Algorithm:
Sentiment analysis will be done on the user reviews to understand public sentiment on these products as well as their intuition behind the reviews. 

### Sentiment Analysis:
For sentiment analysis, the most frequent words are identified first to understand what are the popular topics the users are reviewing about these phones. Next with positive and negative word dictionaries, the words from the text files are matched to find the positive, neutral and negative words. The words are identified with the sentiment score formula, which is:

![senti_score](https://user-images.githubusercontent.com/5343403/42731323-479c5b9c-87d0-11e8-9112-35f34811e1a1.PNG)
If the score is greater than 0, then the word is identified as positive, if the score is equal to 0 then neutral and negative otherwise.
After identifying the positive, negative and neutral words, the intuition behind each group of words is analysed based on popular ideas about the products.  

# Analysis:
The analysis on both the phones based on user reviews are described below:

## iPhone 8:
### Data pre-processing:
After saving the tweets in a csv file (tweets_8.txt) from a Python Pandas data frame, necessary pre-processing is done on the texts in R. First the texts were saved in a corpus and then all the alphabets were converted to lower case. Next all the numbers, punctuations, spaces were removed from the text. Then the English stop-words along with self-defined stop-words were removed from the tweets. In the case of iPhone, the self-defined stop-words decided are "iPhone", "apple", "plus", “phone”, because these words are likely to be appeared in the tweets most. Next stemming is done on the words.

After the above-mentioned processes, the corpus is converted into a term-document matrix which computes the term frequencies of each word in each corpus document. Next the term-document matrix is written in a csv file named “tdm_8.csv”. 

Next the frequencies of each word out of whole corpus is calculated and the top 50 most frequent words are visualized in a word-cloud plot. 
![iphone_top](https://user-images.githubusercontent.com/5343403/42731359-cc74df24-87d0-11e8-809a-d4cb0e4ab970.png)
From the above plot we can see that the top words for iPhone-8 includes words like Samsung and Galaxy, indicating that the competitive Samsung product is mentioned several times in the tweets. Also, we can see the words amp, charger, protector, screen, power which indicate the tweets are mostly about charging and screen protectors for the phone. 

Next the positive and negative words are identified from the tweets using the positive word and negative word dictionary. The words that match with the positive word dictionary are saved in a csv file. This process is done by generating a score for each word defining if the word is positive or not. Likewise, the negative words are identified by the same process and saved for further analysis. Also, the words that don’t fall in any of the categories are identified as neutral words. 

Next the positive, negative and neutral words are visualized to understand the sentiments of the reviewers. Frist, we will analyse the meaning behind the positive words:



