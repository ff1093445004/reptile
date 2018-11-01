# -*- coding:UTF-8 -*-
import json
import time
import os
import requests
from contextlib import closing


class findPhotos(object):
    def __init__(self):
        self.root = './img/'
        self.photo_ids = []
        self.download_server = 'https://unsplash.com/photos/xxx/download?force=true'
        self.target = 'https://unsplash.com/napi/photos?page=self_page&per_page=self_per_page&order_by=latest'

    def get_ids(self):
        for x in range(1, 2):
            target = self.target.replace('self_page', str(x)).replace('self_per_page', str(2))
            req = requests.get(url=target)
            j = json.loads(req.text)
            for n in j:
                self.photo_ids.append(n['id'])
            time.sleep(1)
        print(list(self.photo_ids))

    def download(self, photo_id, filename):
        if not os.path.exists(self.root):
            os.mkdir(self.root)
        target = self.download_server.replace('xxx', photo_id)
        with closing(requests.get(url=target, stream=True)) as r:
            with open('%s%d.jpg' % (self.root, filename), 'ab+') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        f.flush()


if __name__ == '__main__':
    gp = findPhotos()
    print('获取图片连接中:')
    gp.get_ids()
    print('图片下载中:')
    for i in range(len(gp.photo_ids)):
        print('  正在下载第%d张图片' % (i + 1))
        gp.download(gp.photo_ids[i], (i + 1))
