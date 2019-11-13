import requests
from parameters import Query, Token, count, fromDate, toDate
import json2csv as jcsv

# Set parameters in parameters.py

# Authorization using bearer token
headers = {
    'Authorization': 'Bearer '+Token,
}

def search(headers, data):
    '''Search with Twitter API

    Setup Parameters in parameters.py
        Query: search keywords
        Token: bearer token
        count: default search limit for each request, 100
        fromDate: start searching date
        toDate: end searching date

    Premium Search:
        Search the last 31 days
        Search limit is 3,000 tweets

    Args:
        header (dict): bearer token
        data (str): paramters passing to API

    Results:
        list of dict: json data of tweets
        next: token for next page

    Raises:
        Exception: download excess limit error

    Examples:
        >>> r, n = search(headers, data)
    '''
    response = requests.post('https://api.twitter.com/1.1/tweets/search/30day/SearchThirtyDays.json', headers=headers, data=data)

    if response:
        response = response.json()
        return (response['results'], response['next'])
    else:
        response.raise_for_status()

def writeNext(nextStr):
    '''Write token for next page to next.txt

    Instead of relay the token for next page inside program, token is saved in a file, in case we can re-download from any of these pages

    Args:
        nextStr (str): token for next page return from previous API request

    Raises:
        IOError: IO error for writing string to next.txt
    '''
    with open('next.txt', 'a') as next_file:
        next_file.write(nextStr+'\n')

def readNext():
    '''Read last token in next.txt

    Returns:
        str: token for next page

    Raises:
        IOError: IO error for reading token from next.txt
    '''
    try:
        with open('next.txt') as next_file:
            lines = next_file.readlines();
            return lines[-1].strip()
    except:
        return None

def main():
    '''Search and save the tweets to temp.csv file
    
    Each request only allow to download 100 tweets
    Relay token for next page to download 3,000 tweets which is the up limits from Twitter.com
    '''
    try:
        while(True):
            currentNext = readNext()

            if currentNext:
                data = '{"query":"%s","maxResults":"%s","fromDate":"%s","toDate":"%s", "next":"%s"}' % (Query, str(count), fromDate, toDate, currentNext)
            else:
                data = '{"query": "%s" ,"maxResults":"%s","fromDate":"%s","toDate":"%s"}' % (Query, str(count), fromDate, toDate)

            currentResults, nextNext = search(headers, data)
            writeNext(str(nextNext))
                
            if currentNext:
                jcsv.writeCSVBody(currentResults)
            else:
                jcsv.writeCSV(currentResults)
    except Exception as err:
        print(err)

if __name__ == '__main__':
    main()
