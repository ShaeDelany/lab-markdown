
import zipfile

zip_file = 'condensed_2010.json.zip'  
extract_to = 'data'  

# Open and extract the ZIP file
with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall(extract_to)

print(f"ZIP file extracted successfully to {extract_to}")

'''

import json
import pprint

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

print(f'len(data)={len(data)}')  # 36,307

word_counts = {
    'trump': 0, 
    'obama': 0,
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