# A Comparison of iPhone-8 & Samsung Galaxy-S8 by Sentiment Analysis from Product Review
## Introduction
The main idea of this project is to collect user sentiment about 2 very popular necessity products of our day to day lives and compare their user satisfaction level. The products I have chosen for this study is iPhone-8, the newest version of iPhone which is very popular in United states. However, some recent research show that iPhone popularity is declining day by day. The main reasons identified for this declining sale is the brand’s high price range and not being able to meet user satisfaction who are paying the price. 

On the other hand, the usability and feature range of Android phones are improving day by day. There are many products in the market that offer the same features as iPhone but with a much lower price. Thus, user expectations about the product quality and service is also lower for these products. The other product that will be compared in this project along with iPhone-8 is Samsung Galaxy S8, which is considered as having equal features, quality and service range as iPhone 8 but with a much lower price.

The objective of this study is to collect user comments and reviews straight from Twitter, Amazon, Gsmarena sites, which are very popular among people to express their sentiment about various products. This project will compare what are some of the positive and negative sides of these 2 products from user sentiment.

The business problem this project aims to identify is such: what is the user sentiment who are using these two products in their daily lives. Also, what are some of the meanings behind the reviews and what impact those latent meanings might have in the future of these products. From this analysis, both the brands producing these phones can learn the most important aspects that users love and hate about the phones. Thus this project can help the companies improve their products as well as sale and user satisfaction by gaining knowledge from the user sentiment available in the internet. 

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

![iphone_top](https://user-images.githubusercontent.com/5343403/42731397-11663f1e-87d2-11e8-8415-35badef8bce9.png)

From the above plot we can see that the top words for iPhone-8 includes words like Samsung and Galaxy, indicating that the competitive Samsung product is mentioned several times in the tweets. Also, we can see the words amp, charger, protector, screen, power which indicate the tweets are mostly about charging and screen protectors for the phone. 

Next the positive and negative words are identified from the tweets using the positive word and negative word dictionary. The words that match with the positive word dictionary are saved in a csv file. This process is done by generating a score for each word defining if the word is positive or not. Likewise, the negative words are identified by the same process and saved for further analysis. Also, the words that don’t fall in any of the categories are identified as neutral words. 

Next the positive, negative and neutral words are visualized to understand the sentiments of the reviewers. Frist, we will analyse the meaning behind the positive words:

![8_pos](https://user-images.githubusercontent.com/5343403/42731405-417ca2b0-87d2-11e8-81b9-bf953c85ba00.png)

From the top 50 positive words identified from the positive-word dictionary we can see that the words “win”, ”giveaway”, ”deal/deals”, ”freebies”, “free” are mostly talked about in the reviewers. These words indicate that the positive tweets were about various deals offered by different sites for the phones. This can be a strong indication that the price range of the phone is so high that most of the positive/happy tweets are from users who got a good deal or interested to free giveaways happening on the iPhones. 

![8_neg](https://user-images.githubusercontent.com/5343403/42731417-605a47e6-87d2-11e8-9892-d4d551b2265c.png)

Next in the word-cloud of negative words we see that the word “Galaxy” is the most frequent with “Samsung” the second most frequent word in the list. These two words indicate that the users were not happy with the iPhones and comparing the iPhone-8 with Samsung Galaxy phones, which are the main competitors of iPhone in the market. Also, there are several other negative words like “goodbye”, “issue”, “change”, “sad” indicating that the users are talking about switching brands from iPhone to other phones, possibly Samsung Galaxy phone considering the frequency of the words “Samsung” and “Galaxy”. 

![8_neu](https://user-images.githubusercontent.com/5343403/42731420-7a1956ea-87d2-11e8-9669-3187a2580d9d.png)

Next in the neutral word cloud we can see the words “Samsung”, “Galaxy”, “android” indicating that the reviewers might have neutrally comparing the iPhone with Android phones.

Next, the sentiment analysis on the Samsung Galaxy S8 phone has been discussed:

## Samsung Galaxy S8:
The pre-processing part of the tweets for Samsung phone are same as iPhones. As well as the parts of creating term-document matrix and identifying most frequent words. The self-stop words identified for this case are: "Samsung", "galaxy", "plus", "phone", "got", "get", "new", "anonymous", "phones", "just", "can".

![s9_top](https://user-images.githubusercontent.com/5343403/42731429-ced5954a-87d2-11e8-9e6d-c017f60f82fa.png)

Above is the word-cloud for top 50 most frequent words found in the user reviews about Samsung Galaxy S8 phones. Again, here the most frequent word is “iPhone” and “Apple” indicating reviewers are comparing the Samsung galaxy phone with iPhones. Also, the words “edge”, “Note” indicates the Galaxy phones are compared to other Samsung phones from Edge and Note series. Also, the words “Great”, “Best”, “Love” indicates the reviewers are loving the Galaxy phone. The words “camera”, “photos” indicate one of the most popular features of the Galaxy phones which is good picture quality. 

Next the positive, negative and neutral words are identified from the dictionaries and analysed for Samsung Galaxy S8 reviews:

![s9_pos](https://user-images.githubusercontent.com/5343403/42731451-2b2a6370-87d3-11e8-8873-164b0cdfdb64.png)

The top mentioned positve words in this case are camera, screen, quality, fast, ram, price, design, apps, indicating reviewers love these features from the Samsung Galaxy S8 phones. Again the words apple and iphone are seen, which means the comparison between iPhone and Galaxy phone is very popular among the users.

![s9_neg](https://user-images.githubusercontent.com/5343403/42731457-4922e12c-87d3-11e8-9406-2255ee49b885.png)

In the negative reviews there is not much words that can give intuitions about negative user sentiment. However, the words “battery”, “lagging” indicates most of the negative reviews are about smaller battery life and slow speed of the phone.  

![s9_neu](https://user-images.githubusercontent.com/5343403/42731463-6fc65cb4-87d3-11e8-8520-66a2c15eee4c.png)

The neutral reviews also don’t give much intuition about the user sentiment on the Galaxy phones. However the word “Oneplus” is indicating that people are talking about another popular android phone brand that is a major competitor for the samsung phones in Android market. So the business team of Samsung can compare public sentiment on oneplus phones in future to better understand user demand on android phones. 

## Results & Conclusion:
In this project user reviews were collected directly from Twitter and other sites that sell the phones to identify public sentiment on two of the most popular phones at this time. The reviews were collected randomly to prevent any bias from the user side. However, one observation should be mentioned about the source of the data which is reviews collected directly from selling sites (like Amazon or eBay) are more specific and intuitive than tweets collected from Twitter where.  

In the sentiment analysis part of the comparison we have looked at the top mentioned words as well as the positive, negative and neutral words about both the iPhone 8 and Samsung Galaxy S8 phones. The most common factor found after the sentiment analysis is that users are very prone to compare models that come with similar features. So, knowing about pros and cons of the other features can help the individual brands to grow. 

For iPhone, the conclusion after sentiment analysis can be drawn as such: the price range of these phones are a big factor and people are looking for deals and giveaways to buy iPhone. Also, the negative reviews indicate that the Samsung Galaxy phones are mentioned the most along with people talking about changing or switching brand. So, this can be a warning for the brand that Samsung Galaxy phones are a major setback for their market share. 

The sentiment on Samsung Galaxy S8 is mostly about the camera, photos, lagging and battery life. While in the positive reviews, users talk about the design of the phone, ram, speed and camera, in the negative reviews users are complaining about lagging and smaller battery life. So necessary steps should be taken by the brand to improve the user sentiment. 

However, some of the major issues that can be identified from the user reviews by a human are absent in the results of the analysis. For example, both the phones are known for having screens that are broken very easily. While the top words in the analysis consists, words like “protector”, “case”,” screen”, they do not give us any specific intuition about the user sentiment behind using these words in the reviews. But this analysis only indicates the fact that sentiment analysis is not yet perfect and human intuition is needed the most in this area for accurate identification. 

