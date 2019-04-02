from rake_nltk import Rake
import csv

rake = Rake()

titles = []

with open('data/articles.csv') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in reader:
		titles.append(row[0])

rake.extract_keywords_from_sentences(titles)
ranked_phrases_with_scores = rake.get_ranked_phrases_with_scores()

with open('data/ranked_phrases_with_scores.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["score", "phrase"])
    writer.writerows(ranked_phrases_with_scores)

f.close()