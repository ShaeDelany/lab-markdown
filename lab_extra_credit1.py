#!/usr/bin/python3

import json
import pprint
import os

files = [
    'data/tweets_01-08-2021.json',     
]
data = []
for file in files:
    with open(file, encoding='utf8') as fin:
            text = fin.read()
            data.extend(json.loads(text))  

total_tweets = len(data)
print(f'total number of tweets = {len(data)}')  

word_counts = {
    'trump': 0, 
    'obama': 0,
    'mexico': 0,
    'russia': 0,
    'fake news': 0,
    'president': 0,
    'make america great again': 0,
    'immigration': 0,
}
for tweet in data:
    try:
        text = tweet['full_text']
    except KeyError:
        try: 
            text = tweet['text']
        except KeyError:
            text = ''
    if text:
        text_lower = text.lower()
        for word in word_counts:
            if word in text_lower:
                word_counts[word] += 1
pprint.pprint(word_counts)

'''

markdown_table = '|      Phrase     |   Percent of Tweets  |\n'
markdown_table += '|---------------|----------------------|\n'

for word, count in word_counts.items():
    percentage = (count / total_tweets) * 100  
    markdown_table += f"| {word.rjust(16)} | {percentage:6.2f}% |\n"
print(markdown_table)

with open("README2.md", "w", encoding="utf-8") as readme_file:
    readme_file.write("Word Frequency\n\n")
    readme_file.write(f"Total number of tweets by Trump analyzed by from 2009-2019: {total_tweets}\n\n")
    readme_file.write(markdown_table)
'''

lab_dict = {
    'fake news': 940,
    'trump': 18356,
    'obama': 3117,
    'mexico': 353,
    'president': 5107,
    'russia': 744,
    'make america great again': 587,
    'immigration': 335,
}

# x - axis

terms = list(lab_dict.keys())
print(f'terms={terms}')  

# y - axis
counts = list(lab_dict.values())
print(f'counts={counts}')

sorted_terms = []
sorted_counts = []
for i, term in enumerate(sorted(terms)):
    sorted_terms.append(term)
    sorted_counts.append(lab_dict[term])

print(f'sorted_terms={sorted_terms}')
print(f'sorted_counts={sorted_counts}')


# this code generates a plot
import matplotlib.pyplot as plt
plt.bar(sorted_terms, sorted_counts)
plt.subplots_adjust(bottom=0.4)
plt.xticks(rotation=45, ha="right")
plt.xlabel("Word")
plt.ylabel("Counts")
plt.title("Word Frequency in Tweets")

#plt.show()
plt.savefig('Trump_Tweet_Figure2.png')
