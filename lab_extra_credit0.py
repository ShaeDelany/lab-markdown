#!/usr/bin/python3

#"created at"
#Mon,Sun,Sat,Fri,Thu,Wed,Tue

import json
import pprint
import os
from datetime import datetime

files = [
    'data/condensed_2009.json',
    'data/condensed_2010.json',
    'data/condensed_2011.json',
    'data/condensed_2012.json',
    'data/condensed_2013.json',
    'data/condensed_2014.json',
    'data/condensed_2015.json',
    'data/condensed_2016.json',
    'data/condensed_2017.json',
    'data/condensed_2018.json',     
]
data = []
for file in files:
    with open(file, encoding='utf8') as fin:
        text = fin.read()
        data.extend(json.loads(text))  

total_tweets = len(data)
print(f'total number of tweets = {len(data)}')  # 36,307

tweet_counts = {
    'Mon': 0, 
    'Tue': 0,
    'Wed': 0,
    'Thu': 0,
    'Fri': 0,
    'Sat': 0,
    'Sun': 0,
}
for tweet in data:
    try:
        created_at = tweet['created_at']
        dt = datetime.strptime(created_at, '%a %b %d %H:%M:%S %z %Y')
        weekday = weekday = dt.strftime('%a')
        tweet_counts[weekday] += 1
    except:
        print('missing key in tweet', tweet)

pprint.pprint(tweet_counts)

# these are the term counts calculated in the lab
lab_dict = {
    'Mon': 5436, 
    'Tue': 6365,
    'Wed': 6450,
    'Thu': 5919,
    'Fri': 5401,
    'Sat': 3529,
    'Sun': 3207,
    }


# x - axis
terms = list(lab_dict.keys())
print(f'terms={terms}')  

# y - axis
counts = list(lab_dict.values())
print(f'counts={counts}')


print(f'terms={terms}')
print(f'counts={counts}')

# this code generates a plot
import matplotlib.pyplot as plt
plt.bar(terms, counts)
plt.xlabel("Weekday")
plt.ylabel("Counts")
plt.title("Day Frequency in Tweets")

#plt.show()
plt.savefig('Weekday_Figure.png')