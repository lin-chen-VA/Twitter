import csv
#import unicodecsv as csv
import json

def bytes2str(l):
    l2 = []

    for e in l:
        l2.append(str(e))

    return l2

def checkType(array):
    for e in array:
        print(type(e))

def writeHeader(array, writer):
    if len(array) <= 0:
        return False

    header_fields = array[0].keys()
    #header_fields = bytes2str(header_fields)
    #checkType(header_fields)
    writer.writerow(header_fields)

def writeBody(array, writer):
    for tweet in array:
        writer.writerow(tweet.values())

def writeCSV(array):
    with open('temp.csv', 'a') as csv_file:
        writer = csv.writer(csv_file);
        writeHeader(array, writer);
        writeBody(array, writer);

def writeCSVBody(array):
    with open('temp.csv', 'a') as csv_file:
        writer = csv.writer(csv_file);
        try:
            writeBody(array, writer);
        except:
            raise Exception('Error in writing body ...')

def displayColumn(array, columnName):
    for tweet in array:
        print(tweet[columnName])
