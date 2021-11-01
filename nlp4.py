import spacy

nlp = spacy.load("en_core_web_sm")

textfile = open("text for Spacy2.txt", 'r').read()

document = nlp(textfile)

for entity in document.ents:
    print(f"{entity.text}: {entity.label_}")

print(spacy.explain("GPE"))
print(spacy.explain("LOC"))             #similarity method on turnitin to check similarity score

from pathlib import Path

document1 = nlp(Path("RomeoAndJuliet.txt").read_text())
document2 = nlp(Path("EdwardTheSecond.txt").read_text())

print(document1.similarity(document2))  #0.943572424028294 very similar, percentage, shows correlation btw two texts

