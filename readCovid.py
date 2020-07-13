from datetime import date, timedelta, datetime
import time
import csv
import pandas as pd
from twarc import Twarc

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)
start_date = date(2020, 3, 20)
end_date = date(2020, 7, 13) #end date, datetime.date(datetime.now()) (this second option is dynamic and changes by date but depends on timezone)

OAUTH_TOKEN = "1029186921438883845-AQjxqWPxZlURJ47eWFqRFRkSCkDPFh"
OAUTH_TOKEN_SECRET = "YgxeTz31ItxBrJubvwZpZaqa57LLhWRKLMM4t82pdEtsv"
CONSUMER_KEY = "Y70ckEEL2TdQzyq9NqI5RriiB"
CONSUMER_SECRET = "YWQJJlJyzXxkaPXCEdFrANgHFf4Dyd0PtkT4f5TvXFUJLUtpvU"

for date in daterange(start_date, end_date):
    after = date + timedelta(1)
    print(date.strftime("%B%-d").lower()+"_"+after.strftime("%B%-d").lower()+".csv")
    filename=date.strftime("%B%-d").lower()+"_"+after.strftime("%B%-d").lower()+".csv"
    if (date.strftime("%B%-d").lower() != "march29"):
        with open(date.strftime("%B%-d").lower()+"_"+after.strftime("%B%-d").lower()+".csv", 'r') as csvfile:
            data = csv.reader(csvfile, delimiter=' ', quotechar='|')
            """
            for row in data:
                print (row)
                break    
            """
            
            totaldata=pd.read_csv(filename, header=None)
            #for i in totaldata:
            dataframe=totaldata[0]
            print (dataframe)
            numberfile = "number_corona_tweets"+ date.strftime("%B%-d").lower() +".txt"
            readyfile = "ready_corona_tweets"+ date.strftime("%B%-d").lower() +".txt"
            dataframe.to_csv(numberfile, index=False, header=None)
            t = Twarc(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
            for tweet in t.hydrate(open(numberfile)):
                wr = open(readyfile, 'w')
                wr.write(tweet["full_text"])
                #print(tweet["full_text"])
    break

'''
open()

with open('eggs.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
'''
