# Name: Daniel Philipov
# Date: 04/16/2022

import nltk
import json

def manage_url(url, headline=None, author=None, date_publish=None, publication=None, category=None,
                 source_domain=None, article=None, description=None, keyword=None, **kwargs):
    print(f'{url=}')
    print(f'{headline=}')
    print(f'{author=}')
    print(f'{date_publish=}')
    print(f'{publication=}')
    print(f'{category=}')
    print(f'{description=}')
    print('Getting Words...')
    words = nltk.word_tokenize(article)
    print(words)
    print('Getting Sentences...')
    sents = nltk.sent_tokenize(article)
    print(sents)
    print('Getting Contexts...')
    content = nltk.text.Text(words)
    process_keywords(keyword, content)



def process_keywords(keywords, text):
    for keyword in keywords:
        print(f'\x1b[31m{keyword=}\x1b[0m')
        text.common_contexts(keyword)
        print('\x1b[34msimilar\x1b[0m')
        text.similar(keyword)
        print('\x1b[33mconcordance\x1b[0m')
        text.concordance(keyword)


if __name__ == '__main__':
    sites = json.load(open('sites.json', 'r'))

    for site, data in sites.items():
        manage_url(site, **data)
