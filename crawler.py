# *- coding: utf-8 -*-

import time
import requests
import jieba
import re
from bs4 import BeautifulSoup

jieba.set_dictionary('dict.txt.big')  # using Traditional Chinese dict


def crawler():

    boardName = 'stock'
    articleID = ''
    ptt = 'https://www.ptt.cc'

    pttUrl = ptt + '/bbs/' + boardName + '/index' + articleID + '.html'
    # print(pttUrl)
    soup = BeautifulSoup(getRequest(pttUrl).text, "lxml")
    print(soup.prettify())

    for link in soup.find_all('a'):
        try:
            url = ptt + link.get('href')
            print(url)
            href = link.get('href')
            tmp = href.split('/')
            print(tmp)
            indexpattern = re.compile(r'index\d+.html')
            indexmatch = indexpattern.match(tmp[3])
            if indexmatch:
                print(indexmatch.group())
            # parse(url)
            # time.sleep(0.01)
        except:
            print('###except')
            # raw_input()
            print(link.get('href'))


def getRequest(link):
    request = requests.get(url=link, cookies={'over18': '1'})
    if request.status_code != 200:
        print('#######wrong url:', request.url)
        # raw_input()
        return 0
    # pip install pyopenssl ndg-httpsclient pyasn1
    return request


def parse(link):
    soup = BeautifulSoup(getRequest(link).text, "lxml")
    mainContent = soup.find(id="main-content")
    # print mainContent.text
    # for string in mainContent.stripped_strings:
    #    seg_list = jieba.cut(string, cut_all=False)
    #    print("/ ".join(seg_list))


crawler()
