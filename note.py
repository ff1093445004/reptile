# -*- coding:UTF-8 -*-
import requests

if __name__ == '__main__':
    target = 'http://www.biqukan.com/1_1094/5403177.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'https://www.biqukan.com/1_1094/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8,ko;q=0.6',
        'Cookie': 'UM_distinctid=166c8b13b312bf-0c89267367bbce-3e63430c-15f900-166c8b13b3260d; CNZZDATA1260938422=1166608611-1540964183-%7C1540964183; bcolor=; font=; size=; fontcolor=; width=',
        'If-None-Match': '"1518171634"',
        'If-Modified-Since': 'Fri, 09 Feb 2018 10:20:34 GMT'
    }
    req = requests.get(url=target, headers=headers)
    print(req.text)
