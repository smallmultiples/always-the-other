import bs4 as bs
import requests
import re
import csv
import time
from slugify import slugify
import os

titles = []

with open('data/articles.csv') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in reader:
		print(row[0])
		title = row[0]
		filename = "data/articles/%s.txt" % slugify(title)
		file_exists = os.path.isfile(filename)
		if not file_exists:			
			url = row[1]
			sauce = requests.get(url)
			soup = bs.BeautifulSoup(sauce.content,'html.parser')
			try:
				pars = ('').join([p.text for p in soup.find_all("div", class_="article section")[0].select("p")[1:-2]])

				print(pars)
				print('\n\n')
				time.sleep(3)

				f = open(filename,"w+")
				f.write(pars)
				f.close()
			except:
				pass