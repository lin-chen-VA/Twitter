import json
import sys
from TwitterAPI import TwitterAPI
import json2csv as jcsv
from t import ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET
from parameters import Query, Geo, count
 
api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

def writeMinID(id):
    '''Write min id for further search

    Args:
        id (str): min id of the search tweets

    Raises:
        IOError: IO error for writing id to min.txt
    '''
    with open('min.txt', 'a') as min_file:
        min_file.write(str(id)+'\n')

def readMinID():
    '''Read the last tweet id in min.txt

    Returns:
        str: last id from previous search

    Raises:
        IOError: IO error for reading last id of the tweet downloaded from min.txt
    '''
    try:
        with open('min.txt') as min_file:
            lines = min_file.readlines()
            return lines[-1].strip()
    except:
        return None

def search(searchDict):
    '''Search with Twitter API

    Setup Parameters in parameters.py
        Query: search keywords
        Geo: geo location and search range
        count: default search limit for each request, 15

    Standard Search:
        Search the last 7 days
        Search limit is 2,655 tweets

    Args:
        searchDict (dict): search parameters

    Returns:
        a list of dict: json data of tweets

    Raises:
        Exception: error that can not build connection
    '''
    r = api.request('search/tweets', searchDict)

    if r.status_code == 200:
        r = json.loads(r.text)
        results = r['statuses']
        return results
    else:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        raise Exception('Line '+ str(exc_tb.tb_lineno) + ': can not create connection ...')

def main():
    '''Search and save the tweets to temp.csv file

    Each request only allow to download 15 tweets
    Download as many as possible by using the min id of the tweets downloaded in the previous request
    '''
    total = 0
    while(True):
        currentMinID = readMinID()

        if currentMinID:
            searchDict = {'geocode':Geo, 'q':Query}
        else:
            searchDict = {'geocode':Geo, 'q':Query, 'max_id':currentMinID}

        try:
            results = search(searchDict)
        except Exception as err:
            raise Exception(str(err))
        writeMinID(min([result['id'] for result in results]))

        if currentMinID:
            jcsv.writeCSVBody(results)
        else:
            jcsv.writeCSV(results)

        total += len(results)
        print('Has downloaded '+str(total)+' ...')

if __name__ == '__main__':
    try:
        main()
    except Exception as err:
        print(err)
