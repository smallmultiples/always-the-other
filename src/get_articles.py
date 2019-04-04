
import bs4 as bs
import requests
import re
import csv
from selenium import webdriver

browser = webdriver.Chrome(executable_path="env/bin/chromedriver.exe")

articles = []

start_rank = 1

while start_rank <= 3:
	print(start_rank)	
	url = "https://search-beta.abc.net.au/#/?query=\"indian-australian\"&configure%%5BgetRankingInfo%%5D=true&configure%%5BclickAnalytics%%5D=false&configure%%5Banalytics%%5D=false&page=%d&menu%%5BABCSEARCH_globalCategory%%5D=news" % start_rank
	browser.get(url)
	html = browser.execute_script("return document.body.innerHTML")
	soup = bs.BeautifulSoup(html,'html.parser')
	
	raw_results = soup.select('ul')[3].select('li')

	for raw_result in raw_results:
		title = re.sub(r"[\n\t\r]*", "", raw_result.select_one('h2').text)		
		link = raw_result.select_one('article a').get('href')
		articles.append([title, link])
		print(title)
	start_rank += 1

with open('data/indian-australian-articles.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerows(articles)