# -*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    target = 'https://nj.fang.anjuke.com/loupan/s?kw='
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }
    req = requests.get(url=target, headers=headers)
    html = req.text
    bf = BeautifulSoup(html, 'html.parser')
    r = bf.find_all('div', class_='item-mod')
    print(r)
