# Name: Daniel Philipov
# Date: 04/16/2022

import nltk
import json
from typing import List, Tuple, Dict

stopwords = frozenset(nltk.corpus.stopwords.words('english'))

def compare_sents(article1, article2, word) -> dict:
    sents1, sents2 = get_sents(article1), get_sents(article2)
    dict1 = {}
    for sent1 in find_sents(sents1, word):
        for sent2 in find_sents(sents2, word):
            score = cosine_similarity(sent1, sent2)
            dict1[sent1, sent2] = score
    return dict1

def get_sents(article) -> List[str]:
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

def cosine_similarity(sent1, sent2) -> float:
    l1, l2 = [], []
    text1, text2 = nltk.word_tokenize(sent1), nltk.word_tokenize(sent2)
    x_list = set(text1) - stopwords
    y_list = set(text2) - stopwords
    rvector = x_list | y_list
    for w in rvector:
        l1.append(int(w in x_list))
        l2.append(int(w in y_list))
    c = 0
    for i in range(len(rvector)):
        c += l1[i] * l2[i]
    cosine = c / float(sum(l1) * sum(l2))
    return cosine

# makes the dictionary of all pairs
def make_structure(sites=None) -> dict:
    if sites is None:
        sites = json.load(open('sites.json', 'r'))

    common_keywords = set().union(*[set(data['keyword']) for data in sites.values()])

    all_dict = {word: compare_sents(*[data['article'] for data in sites.values()], word) for word in common_keywords}
    # for word, sents in all_dict.items():
    #     if sents:
    #         all_dict[word]['closest'] = *(m := max(sents, key=sents.get)), sents[m]
    return all_dict

# takes the dictionary, returns top 5 and bottom 5
def read_structure(scores) -> Dict[str, Tuple[list, list]]:
    tops = {}
    for word, pairs in scores.items():
        tops[word] = {}
        tops[word]['closest'] = sorted(pairs, key=pairs.get, reverse=True)[:5]
        tops[word]['furthest'] = sorted(pairs, key=pairs.get, reverse=False)[:5]
    with open('tops.json', 'w') as f:
        f.write(json.dumps(tops, indent=4))
    return tops


if __name__ == '__main__':
    from pprint import pprint
    pprint(make_structure())
