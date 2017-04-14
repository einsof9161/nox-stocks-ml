# *- coding: utf-8 -*-

import time
import requests
import jieba
import re
import logging
from bs4 import BeautifulSoup
from gensim.models import word2vec

#     Jieba settings   #
jieba.set_dictionary('dict.txt.big')  # using Traditional Chinese dict
stopwordset = set()
with open('stopwords.txt', 'r') as sw:
    for line in sw:
        stopwordset.add(line.strip('\n'))


boardName = 'Stock'
index = ''
ptt = 'https://www.ptt.cc'
pttUrl = ptt + '/bbs/' + boardName + '/index' + index + '.html'


def crawler(url):
    global index
    soup = BeautifulSoup(getRequest(url).text, "lxml")
    # print(soup.prettify())

    for link in soup.find_all('a'):
        try:
            href = link.get('href')
            hrefsplit = href.split('/')
            # print(hrefsplit)
            indexpattern = re.compile(r'index\d+.html')
            indexmatch = indexpattern.match(hrefsplit[3])
            if indexmatch:
                # print(indexmatch.group())
                if indexmatch.group() > 'index1.html':
                    indexNO = indexmatch.group()
                    indexNO = filter(str.isdigit, indexNO)
                    # print(indexNO)
                    if index == '' or int(index) > int(indexNO):
                        index = indexNO
                    nextpage = (
                        ptt + '/bbs/' + boardName + '/index' + index + '.html'
                    )
                    # if url < pttUrl:
                    #    print('{} < {}'.format(url, pttUrl))
                    #    nextpage = url
                    #    print('nextpage is:{}'.format(nextpage))
            parse(ptt + href)
            # print(ptt + href)
            time.sleep(0.2)
        except:
            pass
            # print('====except====')
            # raw_input()
            # print(link.get('href'))

    crawler(nextpage)


def getRequest(link):
    request = requests.get(url=link, cookies={'over18': '1'})
    if request.status_code != 200:
        print('#######wrong url:', request.url)
        # raw_input()
        return 0
    # pip install pyopenssl ndg-httpsclient pyasn1
    return request


def parse(link):
    print(link)
    soup = BeautifulSoup(getRequest(link).text, "lxml")
    mainContent = soup.find(id="main-content")
    print mainContent.text
    with open("segout.txt", 'a') as out:
        for string in mainContent.stripped_strings:
            seg_list = jieba.cut(string, cut_all=False)
            # print("/ ".join(seg_list))
            for word in seg_list:
                if word not in stopwordset:
                    try:
                        b_str = word.encode('big5')
                        out.write(b_str + '  ')
                        # print word
                    except:
                        print word
                        pass


def ToVec():
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    sentences = word2vec.Text8Corpus("segout.txt")
    print sentences
    model = word2vec.Word2Vec(sentences, size=250)
    model.save("w2v.model.bin")
    # class gensim.models.word2vec.Word2Vec(sentences=None,
    # size=100, alpha=0.025, window=5, min_count=5, max_vocab_size=None,
    # sample=0.001, seed=1, workers=3, min_alpha=0.0001, sg=0, hs=0,
    # negative=5, cbow_mean=1, hashfxn=<built-in function hash>, iter=5,
    # null_word=0, trim_rule=None, sorted_vocab=1, batch_words=10000)


Input = raw_input('input 1 or 2 or 3:')
if Input == '1':
    print ('parsing test, output a word-splitted ptt content')
    site = raw_input('please input a ptt website URL:')
    parse(site)
if Input == '2':
    print('LETS GO, CRAWING EVEYTING')
    crawler(pttUrl)
if Input == '3':
    print('Word2Vec test, not avaliable at the time')
    ToVec()
