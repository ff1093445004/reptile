# -*- coding:UTF-8 -*-
import requests

if __name__ == '__main__':
    target = 'http://www.biqukan.com/1_1094/5403177.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'https://www.biqukan.com/1_1094/',
        'Cookie': 'UM_distinctid=166c8b13b312bf-0c89267367bbce-3e63430c-15f900-166c8b13b3260d; CNZZDATA1260938422=1166608611-1540964183-%7C1540964183; bcolor=; font=; size=; fontcolor=; width='
    }
    req = requests.get(url=target, headers=headers)
    print(req.text)
