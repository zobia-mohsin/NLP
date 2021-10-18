from textblob.sentiments import NaiveBayesAnalyzer
from textblob import TextBlob  # importing module from textblob libraray

text = "Today is a beautiful day. Tomorrow looks like bad weather."
blob = TextBlob(text)

# print(blob.sentences)  # prints results as list of sentence object.
# print(blob.words)  # breaks up into words and make each word an object

# tells us code for each word as in what of the langague it is, verb, noun, etc
# print(blob.tags)

# print(blob.noun_phrases)

# SENTIMENT ANALYSIS, how do you interpret words good and bad. Not so bad vs was bad

# results are two values as the entire phrase
#print(round(blob.sentiment.polarity, 3))
# is evaluteeed as one from -1 to 1 for polarity. How subject it is?, the closer to one the more positive it is
#print(round(blob.sentiment.subjectivity, 3))

sentences = blob.sentences

# for sentence in sentences:
#   print(sentence)
#    print(round(sentence.sentiment.polarity, 3))

# not perfect, based on movie reviews, differetn analyzer so different format
blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())

# print(blob.sentiment)

for sentence in blob.sentences:
    print(sentence.sentiment)

# LANGAUGE DETECTION AND LANGUAGE TRANSACTION
spanish = blob.translate(to='zh')

print(spanish)
