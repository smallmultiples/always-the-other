
import bs4 as bs
import requests
import re
import csv

articles = []

start_rank = 1

while start_rank <= 141:
	print(start_rank)
	url = "http://search.abc.net.au/s/search.html?query=%22chinese-australian%22&collection=news_meta&form=simple&gscope1=10&start_rank=" + str(start_rank)
	sauce = requests.get(url)
	soup = bs.BeautifulSoup(sauce.content,'html.parser')
	
	raw_results = soup.select('ol')[0].select('li')
	for raw_result in raw_results:
		title = re.sub(r"[\n\t\r]*", "", raw_result.select_one('h3').text)		
		link = raw_result.select_one('h3 a').get('href')
		articles.append([title, link])
		print(title)
	start_rank += 10

with open('data/articles.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(articles)