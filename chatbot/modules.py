# -*- coding: utf-8 -*-
"""
Reg No: R157690W
Course : CTH (Honours in Computer Science)
Chatbot Functions Which integratable on any platform
"""
from bs4 import BeautifulSoup
import requests
import urllib.parse
from urllib.request import urlopen
import feedparser
import simplejson as json
import wikipedia


## ** Chatbot Functions **
def get_wikipedia(wiki_query):
	""" gets a wikipedia entry with :
		wiki.title (Name of the wikipedia page), 
		wiki.summary (a short version of the wikipedia content),
		wiki.url (the http address where the wikipedia page can be found) and
		wiki.content (The full text entry of the wikipedia page)
	"""
	try:
		wiki = wikipedia.page(wiki_query) # search wikipedia for a page matching the input string
	except:
		wiki = None

	return wiki


def get_news(news_query):
	""" get the latest headlines using google news rss feed feature  """
	s_string = urllib.parse.quote_plus(news_query)	# make the news query into url friendly parameters
	url = 'http://news.google.com/news?hl=en&q='+s_string+'&output=rss' 
	feed = feedparser.parse(url) # fetch google news feed with the search query in search string
	news_articles = []
	for post in feed.entries:
		post_content_raw = post.summary
		clean_content = BeautifulSoup(post_content_raw, "lxml").get_text(" ") #strip html characters and add whitespace to prettify content
		news_articles.append({'headline' : post.title, 'content': clean_content})
	return news_articles


def get_photo(photo_query):
	""" get the latest headlines by scraping the openphoto.net site  """
	s_string = urllib.parse.quote_plus(photo_query)	# make the news query into url friendly parameters
	url = 'http://openphoto.net/search/index.html?search_text='+s_string+'&post=1' 
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'lxml')
	link = soup.find(class_='op-thumbs')
	print(type(link))
	#check if the link isn't empty
	if link is not None:
		print(link.get('src'))
		return link.get('src')

	elif link is None:
		return "https://media.giphy.com/media/xT0BKmtQGLbumr5RCM/giphy.gif"


def get_kgsearch(search_query):
	""" search for relevant information using the Google Knowledge Graph API. wikipedia seems to have better results though.... """
	Key = 'AIzaSyDF8KMv8xXze_CAZM9LExCnRYSW5h7WITE' ## Stricter security measures will be implemeted later for the key
	i = search_query
	i = urllib.parse.quote(i)
	link = json.load(
		urlopen("https://kgsearch.googleapis.com/v1/entities:search?query=" + i + "&key=" + Key + "&limit=1&indent=True"))
	Output = link['itemListElement']

	for element in Output:
		if '@type' in element['result']:
			word_type = element['result']['@type']
		if "description" in element['result']:
			description = element['result']['description']
		if "detailedDescription" in element['result']:
			article_url = element['result']['detailedDescription']['url']
			articleBody = element['result']['detailedDescription']['articleBody']
		else:
			articleBody =''
			article_url =''	
		if 'name' in element['result']:
			name = element['result']['name']
		
		# Output results
		search_results = {
			'name': name, 
			'description': description, 
			'content': articleBody, 
			'source': article_url 
		}
		return search_results
