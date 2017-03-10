# *- coding: utf-8 -*-

import time
import requests
import jieba
import re
from bs4 import BeautifulSoup

jieba.set_dictionary('dict.txt.big')  # using Traditional Chinese dict

boardName = 'stock'
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
            # parse(url)
            print(ptt + href)
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
    soup = BeautifulSoup(getRequest(link).text, "lxml")
    mainContent = soup.find(id="main-content")
    # print mainContent.text
    # for string in mainContent.stripped_strings:
    #    seg_list = jieba.cut(string, cut_all=False)
    #    print("/ ".join(seg_list))


crawler(pttUrl)
