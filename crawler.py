# *- coding: utf-8 -*-

import time
import requests
from bs4 import BeautifulSoup


def crawler():

    boardName = 'stock'
    articleID = ''
    ptt = 'https://www.ptt.cc'

    pttUrl = ptt + '/bbs/' + boardName + '/index' + articleID + '.html'
    print(pttUrl)
    soup = BeautifulSoup(getRequest(pttUrl).text, "lxml")
    print(soup.prettify())

    for link in soup.find_all('a'):
        try:
            url = ptt + link.get('href')
            print(url)
            parse(url)
            time.sleep(0.01)
        except:
            print('except')
            print(link.get('href'))


def getRequest(link):
    request = requests.get(url=link, cookies={'over18': '1'})
    if request.status_code != 200:
        print('wrong url:', request.url)
        return 0
    # pip install pyopenssl ndg-httpsclient pyasn1
    return request


def parse(link):
    soup = BeautifulSoup(getRequest(link).text, "lxml")
    mainContent = soup.find(id="main-content")
    print mainContent.text


crawler()
