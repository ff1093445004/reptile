from selenium import webdriver
from lxml import etree
import json
import redis
import time


class zhangui(object):
    def __init__(self):
        # https://ju.taobao.com/json/tg/ajaxGetItemsV2.json?callback=define&page=1&psize=20&type=0&algorithm_scene=juWapHome&frontCatId=1000
        # https://ju.taobao.com/json/tg/ajaxGetItemsV2.json?callback=define&page=1&psize=20&type=0&algorithm_scene=juWapHome&frontCatId=7000
        # https://ju.taobao.com/json/tg/ajaxGetItemsV2.json?callback=define&page=1&psize=20&type=0&algorithm_scene=juWapHome&frontCatId=43000
        self.url = "https://ju.taobao.com/json/tg/ajaxGetItemsV2.json?callback=define&page={}&psize=20&type=0&algorithm_scene=juWapHome&frontCatId=1000"
        self.header = {
            "user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 10 Build/MOB31T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
            "referer": "https://jhs.m.taobao.com/m/list.html?_loc=JU_WAP_CAT_43000&spm=a2147.7632989.Topbar.d43000",
            "cookie": "miid=1033132151657299625; bid=2; thw=cn; cna=c1CJE47NgxoCAXpgKjoVXt3e; t=1fd0a7e50c4621965534c626d0c1ac49; jxwebp=1; cookie2=42e1f7489e8417caf9ddc74f589b8641; v=0; _m_h5_tk=500a923b9d9f7e5c9b07aaedb4c85afc_1543566368474; _m_h5_tk_enc=25691cb57cda2467df544b5e34ced0de; codefold_time=1543557731927; uc1=cookie14=UoTYNc5xYAdeWg%3D%3D; _tb_token_=qOUbowutkpC2c7Rw2whv; isg=BCQklGgmJJduAVckYiW0IVRO9SLWFVcHzDh_jD5FsO_j6cSzZs0Yt1oPrUdxMYB_"
        }

    def downLoad(self):
        browser = webdriver.Chrome()
        pl = []
        for i in range(1, 2):
            browser.get(self.url.format(i))
            h = browser.page_source
            html = etree.HTML(h)
            text = html.xpath("//pre/text()")[0]
            jsonObj = json.loads(text.strip().replace("define", "")[1:-1])
            result = jsonObj["itemList"]
            for p in result:
                pp = product(p["baseinfo"]["itemId"], p["name"]["shortName"], p["name"]["longName"],
                             p["price"]["origPrice"],
                             p["extend"]["brandName"],
                             p["merit"]["desc"])
                pl.append(pp)
            time.sleep(1)
        browser.close()
        return pl

    def save(self, pl):
        pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
        r = redis.Redis(connection_pool=pool)
        for i, p in enumerate(pl):
            print(str(i) + ":" + str(p.id))
            r.set(p.id, json.dumps(p, default=o2j, ensure_ascii=False))


class product(object):
    def __init__(self, id, name, desc, price, producer, tags):
        self.id = id
        self.name = name
        self.desc = desc
        self.price = price
        self.producer = producer
        self.tags = tags


def o2j(p):
    return {
        "id": p.id,
        "name": p.name,
        "desc": p.desc,
        "price": p.price,
        'producer': p.producer,
        "tags": p.tags
    }


if __name__ == '__main__':
    zr = zhangui()
    productList = zr.downLoad()
    zr.save(productList)
    print("=============完成=============")
