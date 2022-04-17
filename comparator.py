# Name: Daniel Philipov
# Date: 04/16/2022

import nltk
import json
from typing import Tuple

stopwords = set(nltk.corpus.stopwords.words('english'))

def manage_url(url, headline=None, author=None, date_publish=None, publication=None, category=None,
                article=None, description=None, keyword=None, **kwargs):
    print(f'{url=}')
    print(f'{headline=}')
    print(f'{author=}')
    print(f'{date_publish=}')
    print(f'{publication=}')
    print(f'{category=}')
    print(f'{description=}')

def compare_sents(article1, article2, word) -> Tuple[dict, dict]:
    sents1, sents2 = get_sents(article1), get_sents(article2)
    dict1 = dict2 = {}
    for sent1 in find_sents(sents1, word):
        for sent2 in find_sents(sents2, word):
            score = cosine_similarity(sent1, sent2)
            dict1[sent1] = (sent2, score)
            dict2[sent2] = (sent1, score)
    return dict1, dict2

def get_sents(article):
    return nltk.sent_tokenize(article)

def process_keywords(keywords, text):
    for keyword in keywords:
        print(f'\x1b[31m{keyword=}\x1b[0m')
        text.common_contexts([keyword])
        print('\x1b[34msimilar\x1b[0m')
        text.similar(keyword)
        print('\x1b[33mconcordance\x1b[0m')
        text.concordance(keyword)

def find_sents(sents, word):
    word = word.lower()
    for sent in sents:
        if word in sent.lower():
            yield sent

def cosine_similarity(text1, text2) -> float:
    return nltk.cluster.util.cosine_distance(text1, text2)

if __name__ == '__main__':
    sites = json.load(open('sites.json', 'r'))

    common_keywords = set().union(*[set(data['keyword']) for data in sites.values()])
    for site, data in sites.items():
        manage_url(site, **data)

    all_dict = {word: compare_sents(*[data['article'] for data in sites.values()], word) for word in common_keywords}
    all_dict['closest'] = (m := max(all_dict.items(), key=lambda e: e[1][1]))[0], m[1][0]
    json.dump(all_dict, open('words_comparison.json', 'w'))
