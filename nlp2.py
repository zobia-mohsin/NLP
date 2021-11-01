from textblob import TextBlob
import nltk
from pathlib import Path
import pandas as pd


nltk.download("stopwords")
from nltk.corpus import stopwords

stops= stopwords.words("english")

#print(stops)

blob = TextBlob ("Today is a beautiful day.")

print(blob.words)

#take list blob.words and go through words also is stopwords and get rid of them put rest in cleanlist
cleanlist = [word for word in blob.words if word not in stops] #put expression word in the very front since no expression
print(cleanlist) #output: ['Today', 'beautiful', 'day']

blob = TextBlob(Path("RomeoAndJuliet.txt").read_text())

#print(blob.words.count("joy")) #output 14 

print(blob.word_counts['juliet'])

more_stops = ['thee', 'thy', 'thou']

stops += more_stops

items = blob.word_counts.items()

#print(items)

clean_items = [i for i in items if i[0] not in stops]

print(clean_items[:10])

from operator import itemgetter

sorted_items = sorted(clean_items) #sorted function has additional argumetns we can use (sort by numbers)

print(sorted_items[:10]) #default sort alphabetical

sorted_items = sorted(clean_items, key =itemgetter(1), reverse = True) #1 pick second element in each tuple as the key for the sort
#reverse for descending order
print(sorted_items[:10])

top20 = sorted_items[:20]

df = pd.DataFrame(top20, columns=['word','count'])

print(df)

import matplotlib.pyplot as plt

df.plot.bar(x='word', y='count', legend = False, color = ['y','c','m','b','g','r'])

plt.gcf().tight_layout()
plt.show()