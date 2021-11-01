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

#for sentence in blob.sentences:
    #print(sentence.sentiment)

# LANGAUGE DETECTION AND LANGUAGE TRANSACTION
spanish = blob.translate(to='es')
chinese = blob.translate(to='zh')

print(spanish)

print(spanish.translate)

print(chinese.translate)


from textblob import Word

index = Word('index')
'''
print(index.pluarlize())

cacti = Word('cacti')

print(cacti.singularize())

animals = TextBlob('dog cat fish bird').words

print(animals.pluralize())

#spellcheck and correction

word = Word('theyr')

print(word.spellcheck())

print(word.correct())

word1 = Word("studies")

word2 = Word("varieties")

print(word1.stem())
print(word2.stem())

print(word1.lemmatize())
print(word2.lemmatize())
'''
#Definitions, synonyms and Antonyms from wodkits

happy = Word("happy")

#print(happy.definitions)


print(happy.synsets) #result is a list, extract text out of list by diong the following below

for s in happy.synsets:
    for lemma in s.lemmas():
        print(lemma.name)

synonym = happy.synsets[1].lemmas()[0].name() #gives second word, index 1
print(synonym)

antonym = happy.synsets[0].lemmas()[0].antonyms()[0]() #gives second word, index 1
print(antonym)