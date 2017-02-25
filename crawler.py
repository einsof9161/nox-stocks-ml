# *- coding: utf-8 -*-

import requests
import lxml
from bs4 import BeautifulSoup

requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'


boardName = 'stock'
articleID = ''
ptt = 'https://www.ptt.cc'

pttUrl = ptt + '/bbs/' + boardName + '/index' + articleID + '.html'
print(pttUrl)

request = requests.get(url=pttUrl, cookies={'over18': '1'})
if request.status_code != 200:
    print('wrong url:', request.url)
# pip install pyopenssl ndg-httpsclient pyasn1

soup = BeautifulSoup(request.text, "lxml")
print(soup.prettify())

for link in soup.find_all('a'):
    try:
        url = ptt + link.get('href')
        print(url)

    except:
        print('except')
        print(link.get('href'))
     #  parse()


# def parse(link)
