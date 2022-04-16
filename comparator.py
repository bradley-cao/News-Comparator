# Name: Daniel Philipov
# Date: 04/16/2022

import nltk
import json
import spacy
import sys


stopwords = set(nltk.corpus.stopwords.words('english'))

def manage_url(url, headline=None, author=None, date_publish=None, publication=None, category=None,
                 source_domain=None, article=None, description=None, keyword=None, **kwargs):
    print(f'{url=}')
    print(f'{headline=}')
    print(f'{author=}')
    print(f'{date_publish=}')
    print(f'{publication=}')
    print(f'{category=}')
    print(f'{description=}')
    # print('Getting Words...')
    words = nltk.word_tokenize(article)
    # print(words)
    # print('Getting Sentences...')
    sents = nltk.sent_tokenize(article)
    # print(sents)
    # print('Getting Contexts...')
    content = nltk.text.Text(words)
    # process_keywords(keyword, content)

def process_keywords(keywords, text):
    for keyword in keywords:
        print(f'\x1b[31m{keyword=}\x1b[0m')
        text.common_contexts([keyword])
        print('\x1b[34msimilar\x1b[0m')
        text.similar(keyword)
        print('\x1b[33mconcordance\x1b[0m')
        text.concordance(keyword)

def find_sents(sents, word):
    for sent in sents:
        if word in sent:
            yield sent

def cosine_similarity(text1, text2) -> float:
    return nltk.cluster.util.cosine_distance(text1, text2)

if __name__ == '__main__':
    sites = json.load(open('sites.json', 'r'))

    common_keywords = set().union(*[set(data['keyword']) for data in sites.values()])
    for site, data in sites.items():
        manage_url(site, **data)
