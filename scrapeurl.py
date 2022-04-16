import sys
import json
from newsfetch.news import newspaper
import requests

if __name__ == '__main__':
    fulldict = dict()
    url1 = sys.argv[1]
    url2 = sys.argv[2]
    get = requests.get(url1)
    get2 = requests.get(url2)
    failed = False
    if get.status_code == 404:
        print(1)
        failed = True
    if get2.status_code == 404:
        print(2)
        failed = True
    if failed == True:
        sys.exit(1)

    news = newspaper(url1)
    news2 = newspaper(url2)
    url1dict = dict()
    url1dict['headline'] = news.headline
    url1dict['author'] = news.authors
    url1dict['article'] = news.article
    url1dict['date_publish'] = news.date_publish
    url1dict['publication'] = news.publication
    url1dict['description'] = news.description
    url1dict['keyword'] = news.keywords
    url1dict['category'] = news.category

    url2dict = dict()
    url2dict['headline'] = news2.headline
    url2dict['author'] = news2.authors
    url2dict['article'] = news2.article
    url2dict['date_publish'] = news2.date_publish
    url2dict['publication'] = news2.publication
    url2dict['description'] = news2.description
    url2dict['keyword'] = news2.keywords
    url2dict['category'] = news2.category

    fulldict[url1] = url1dict
    fulldict[url2] = url2dict

    json_object = json.dumps(fulldict, indent=4)
    with open("sites.json", "w") as outfile:
        outfile.write(json_object)

        

        


