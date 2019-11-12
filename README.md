# <center>Twitter Search</center>

## Description
    A Python script to download tweets from twitter.com.
    
    Early November 2019, Dr. Lu in Department of Geosciences would like to make a study on Hurricane Maria based on tweets at Twitter. Initially, we tried python-twitter and TwitterAPI to download data. However, we realized that both them do not support premium download from Twitter well. The standard supported by them only allow us to download the data last seven days. Thus, we created this script for our purpose.
    
    Last modified on 11.12.2019
    
## Implementation
1. Download new
    
    If there is a next.txt and temp.csv exist, remove them.
> python psearch.py
2. Continue download
    
    Download using the token generated from previous request
> python psearch.py

## Requirements
1. Python 3 installed
2. requests
3. csv

## Download Twitter
1. Standard
> Free, 7 days
2. Premium
> 30 days, free, up to 3,000 tweets
> from 2006, paid, # of limits is unknown
3. Enterprise
> 30 days, paid
> from 2006, paid

## Reference
1. <a href = "https://developer.twitter.com/en/docs/tweets/search/api-reference/premium-search">Search Tweets</a>
