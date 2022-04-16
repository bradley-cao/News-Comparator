# Name: Daniel Philipov
# Date: 04/16/2022

import nltk
import pickle
import json

def manage_url(url, headline=None, author=None, date_published=None, publisher=None, category=None,
                 source_domain=None, article=None, description=None, keyword=None, **kwargs):
    print(f'{url=}')
    print(f'{headline=}')
    print(f'{author=}')
    print(f'{date_published=}')
    print(f'{publisher=}')
    print(f'{category=}')
    print(f'{source_domain=}')
    print(f'{description=}')
    content = nltk.text.Text(article)
    print('Getting Words...')
    words = nltk.word_tokenize(article)
    print('Getting Sentences...')
    sents = nltk.sent_tokenize(article)
    print('Getting Contexts...')
    process_keywords(keyword, content)



def process_keywords(keywords, text):
    for keyword in keywords:
        print(f'{keyword=}')
        text.common_contexts(keyword)
        print('similar')
        text.similar(keyword)
        print('concordance')
        text.concordance(keyword)


if __name__ == '__main__':
    sites = json.load(open('sites.json', 'r'))
    for site, data in sites:
        manage_url(site, **data)
