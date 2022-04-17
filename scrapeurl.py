import sys
import json
import requests
import unidecode
from urllib.request import urlopen
from newsfetch.news import newspaper
from bs4 import BeautifulSoup

def scrape_urls(url1, url2):
    fulldict = dict()
    try:
        html1 = urlopen(url1)
        html2 = urlopen(url2)
    except:
        return "Error"

    data1 = requests.get(url1)
    data2 = requests.get(url2) 
    soup1 = BeautifulSoup(data1.text, 'html.parser')
    soup2 = BeautifulSoup(data2.text, 'html.parser')
    article1 = ""
    article2 = ""
    data = '' 
    for data in soup1.find_all("p"): 
        article1 = article1 + " " + data.get_text()
    data = '' 
    for data in soup2.find_all("p"): 
        article2 = article2 + " " + data.get_text()
    article1 = article1.strip()
    article2 = article2.strip()
    article1 = unidecode.unidecode(article1)
    article2 = unidecode.unidecode(article2)
    article1 = article1.replace("\n", "")
    article2 = article2.replace("\n", "")

    news = newspaper(url1)
    news2 = newspaper(url2)
    url1dict = dict()
    url1dict['headline'] = news.headline
    url1dict['author'] = news.authors
    url1dict['article'] = article1
    url1dict['date_publish'] = news.date_publish
    url1dict['publication'] = news.publication
    url1dict['description'] = news.description
    url1dict['keyword'] = news.keywords
    url1dict['category'] = news.category

    url2dict = dict()
    url2dict['headline'] = news2.headline
    url2dict['author'] = news2.authors
    url2dict['article'] = article2
    url2dict['date_publish'] = news2.date_publish
    url2dict['publication'] = news2.publication
    url2dict['description'] = news2.description
    url2dict['keyword'] = news2.keywords
    url2dict['category'] = news2.category

    fulldict = {url1: url1dict, url2: url2dict}
    returndict = [url1dict, url2dict]
    json_object = json.dumps(fulldict, indent=4)
    with open("sites.json", "w+") as outfile:
        outfile.write(json_object)
        
    return returndict
