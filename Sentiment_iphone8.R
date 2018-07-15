library(tm)
library(pdftools)
library(qdapTools)
library(stringr)
#library(SnowballC)
library(wordcloud)
library(Matrix)
#library(lsa)
library(RColorBrewer)

filepath <-"C:\\ttu\\summer 18\\dataMinning\\p"
setwd(filepath)
file<-'tweets_8.txt'
text = file(file,open="r")
text.decomposition =readLines(text)
text.decomposition[1]
text.decomposition[2]
corpus <- Corpus(VectorSource(text.decomposition)) # colection of documents containing texts 
corpus

corpus <-tm_map(corpus,PlainTextDocument)
corpus <-tm_map(corpus,tolower)
corpus <-tm_map(corpus,removeNumbers) 


stopwords("english")
selfstopwords <- c("iphone","apple", "plus", "phone","now", "charger")
corpus <- tm_map(corpus,removeWords, c(stopwords("english"), selfstopwords))
writeLines(as.character(corpus[[2]]))


corpus <-tm_map(corpus,removePunctuation)
corpus <-tm_map(corpus,stripWhitespace)
writeLines(as.character(corpus[[2]]))

corpus.tdm <-TermDocumentMatrix(corpus)
colnames(corpus.tdm)<-(1:dim(corpus.tdm)[2])
write.csv(as.matrix(corpus.tdm),file=file.path("sentimentAnalysis\\tdm_8.csv"))

frequency <- rowSums(as.matrix(corpus.tdm))
frequency <- sort(frequency, decreasing=TRUE)
head(frequency)
words <- names(frequency)
wordcloud(words[1:50], frequency[1:50],
          scale = c(2, 0.9),colors=brewer.pal(8,"Dark2")) # color palette 


positives= readLines("positive-words.txt") #dictionary: we match if theres more +ve/-ve words in our doc 
negatives = readLines("negative-words.txt")

which_pos <-Terms(corpus.tdm) %in% positives
which_neg <- Terms(corpus.tdm) %in% negatives 

#find the +ve documents and save the matrix 
score_pos <- colSums(as.matrix(corpus.tdm[which_pos, ])) 
score_neg <- colSums(as.matrix(corpus.tdm[which_neg, ]) )
score<-score_pos-score_neg
score

tdm_pos<-corpus.tdm[ ,score>0]
write.csv(as.matrix(tdm_pos),file=file.path("sentimentAnalysis\\tdm_8_pos.csv"))

tdm_neg<-corpus.tdm[ ,score<0]
write.csv(as.matrix(tdm_neg),file=file.path("sentimentAnalysis\\tdm_8_neg.csv"))
# find the neutral docs and save the matrix 
tdm_neu<-corpus.tdm[ ,score==0]
write.csv(as.matrix(tdm_neu),file=file.path("sentimentAnalysis\\tdm_8_neu.csv"))

# plot positive word cloud 
frequency_pos <- rowSums(as.matrix(tdm_pos))
frequency_pos <- sort(frequency_pos, decreasing=TRUE)
words_pos <- names(frequency_pos)
wordcloud(words_pos[1:50], frequency_pos[1:50], scale = c(2, 0.9), colors=brewer.pal(8,"Dark2"))

# plot negative word cloud 
frequency_neg <- rowSums(as.matrix(tdm_neg))
frequency_neg <- sort(frequency_neg, decreasing=TRUE)
words_neg <- names(frequency_neg)
wordcloud(words_neg[1:50], frequency_neg[1:50], scale = c(2, 0.9), colors=brewer.pal(8,"Dark2"))

# neutral 
frequency_neu <- rowSums(as.matrix(tdm_neu))
frequency_neu <- sort(frequency_neu, decreasing=TRUE)
words_neu <- names(frequency_neu)
wordcloud(words_neu[1:50], frequency_neu[1:50], scale = c(2, 0.9), colors=brewer.pal(8,"Dark2"))



