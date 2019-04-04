from textblob import TextBlob
import os
import csv
import re
import spacy

spacy_nlp = spacy.load('en')

path = 'data/articles/indian-australian'

files = []

sentiment = []
counts = []
entities = {}

def clean_text(t):
	cleaned = re.compile("Alert moderator\n").split(t)[0]
	# cleaned = cleaned.split('Topics:')[0]
	# import pdb;pdb.set_trace()
	cleaned = re.compile("Topics:\n").split(cleaned)[0]
	return cleaned

def clean_word(w):
	cleaned = w.replace("\'s ", "")
	cleaned = cleaned.replace("\'s", "")
	cleaned = cleaned.replace("Australians", "australian")
	cleaned = cleaned.replace("australians", "australian")
	cleaned = cleaned.replace("Australian", "australian")
	return cleaned

def build_entities(t):
	for entity in spacy_nlp(t).ents:
		entities[entity.string.strip().lower()] = entity.label_
	return

def get_entity(w):
	entity = None
	try:
		entity = entities[w]
	except:
		pass
	return entity

for r, d, f in os.walk(path):
	for file in f:
		if '.txt' in file:
			files.append(os.path.join(r, file))


with open('data/indian-australian-counts.csv', 'w') as output:
	writer = csv.writer(output)
	writer.writerow(["word","count","entity"])
	for f in files:
		f = open(f, "r")
		print(f.name)
		text = f.read()
		cleaned = clean_text(text)
		blobs = TextBlob(cleaned)
		build_entities(cleaned)
		# import pdb;pdb.set_trace()
		polarity = blobs.sentiment.polarity
		subjectivity = blobs.sentiment.subjectivity
		# sentiment.append([f.name.replace('data/articles/',''), polarity, subjectivity])
		# import pdb;pdb.set_trace()
		for word in blobs.noun_phrases:
			cleaned_word = clean_word(word)
			if cleaned_word:
				entity = get_entity(cleaned_word)
				print(cleaned_word, blobs.noun_phrases.count(word), entity)
				writer.writerow([cleaned_word, blobs.noun_phrases.count(word), entity])
output.close()


# with open('data/sentiment.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerow(["article","polarity","subjectivity"])
#     writer.writerows(sentiment)
# f.close()


