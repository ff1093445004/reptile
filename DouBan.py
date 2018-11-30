import requests
import json


class douBan(object):
    def __init__(self):
        self.target = 'https://read.douban.com/j/category/top?start={}&limit=10'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
        }

    def download(self):
        for i in range(1, 5):
            target = self.target.format(i)
            req = requests.get(target, headers=self.headers)
            j = json.loads(req.text)
            with open('wenjian.txt', 'a', encoding='utf-8') as f:
                f.write(json.dumps(j, ensure_ascii=False, indent=2))
                f.write('\n')
        

if __name__ == '__main__':
    dou_ban = douBan()
    dou_ban.download()
