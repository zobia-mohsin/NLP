from textblob import TextBlob
import nltk
from pathlib import Path
import pandas as pd
import imageio
from wordcloud import WordCloud
from nltk.corpus import stopwords
from operator import itemgetter

#nltk.download("stopwords")

stops= stopwords.words("english")

blob = TextBlob(Path("book of John text.txt").read_text())
#words = blob.noun_phrases
more_stops = ['thy', 'ye', 'verily', 'thee', 'hath', 'say', 'thou', 'art', 'shall']

stops += more_stops
items = blob.word_counts.items()
nouns = blob.noun_phrases

clean_items = [i for i in items if i[0] not in stops if i[0] in nouns]

top15 = str(clean_items[:15])

mask_image = imageio.imread('mask_heart.png') #making an image object for us
wordcloud = WordCloud(colormap = 'prism', mask = mask_image, background_color = 'white')
wordcloud= wordcloud.generate(top15)
wordcloud = wordcloud.to_file('book of John text.png')

print('Done')