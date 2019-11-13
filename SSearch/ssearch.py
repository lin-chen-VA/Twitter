import json
import sys
from TwitterAPI import TwitterAPI
import json2csv as jcsv
from t import ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET
from parameters import Query, Geo, count
 
api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

def writeMinID(id):
    with open('min.txt', 'a') as min_file:
        min_file.write(str(id)+'\n')

def readMinID():
    try:
        with open('min.txt') as min_file:
            lines = min_file.readlines()
            return lines[-1].strip()
    except:
        return None

def search(searchDict):
    r = api.request('search/tweets', searchDict)

    if r.status_code == 200:
        r = json.loads(r.text)
        results = r['statuses']
        return results
    else:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        raise Exception('Line '+ str(exc_tb.tb_lineno) + ': can not create connection ...')

def main():
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

        total += len(reuslts)
        print('Has downloaded '+str(total)+' ...')

if __name__ == '__main__':
    try:
        main()
    except Exception as err:
        print(err)
