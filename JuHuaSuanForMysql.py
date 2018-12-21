from selenium import webdriver
from lxml import etree
import json
import time
import pymysql


class zhangui(object):
    def __init__(self):
        # self.url = "https://ju.taobao.com/json/tg/ajaxGetItemsV2.json?callback=define&page=1&psize=20&type=0&algorithm_scene=juWapHome&frontCatId=1000"
        # self.url = "https://ju.taobao.com/json/tg/ajaxGetItemsV2.json?callback=define&page=1&psize=20&type=0&algorithm_scene=juWapHome&frontCatId=7000"
        # self.url = "https://ju.taobao.com/json/tg/ajaxGetItemsV2.json?callback=define&page=1&psize=20&type=0&algorithm_scene=juWapHome&frontCatId=43000"
        self.url = "https://ju.taobao.com/json/tg/ajaxGetItemsV2.json?callback=define&page={}&psize=20&type=0&algorithm_scene=juWapHome&frontCatId=1000"
        self.header = {
            "user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 10 Build/MOB31T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
            "referer": "https://jhs.m.taobao.com/m/list.html?_loc=JU_WAP_CAT_43000&spm=a2147.7632989.Topbar.d43000",
            "cookie": "miid=1033132151657299625; bid=2; thw=cn; cna=c1CJE47NgxoCAXpgKjoVXt3e; t=1fd0a7e50c4621965534c626d0c1ac49; jxwebp=1; cookie2=42e1f7489e8417caf9ddc74f589b8641; v=0; _m_h5_tk=500a923b9d9f7e5c9b07aaedb4c85afc_1543566368474; _m_h5_tk_enc=25691cb57cda2467df544b5e34ced0de; codefold_time=1543557731927; uc1=cookie14=UoTYNc5xYAdeWg%3D%3D; _tb_token_=qOUbowutkpC2c7Rw2whv; isg=BCQklGgmJJduAVckYiW0IVRO9SLWFVcHzDh_jD5FsO_j6cSzZs0Yt1oPrUdxMYB_"
        }

    def downLoad(self):
        browser = webdriver.Chrome()
        pl = []
        for i in range(1, 11):
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
                             p["baseinfo"]["picUrl"],
                             p["merit"]["desc"])
                pl.append(pp)
            time.sleep(1)
        browser.close()
        return pl


class product(object):
    def __init__(self, pid, name, des, price, producer, img, tags):
        self.id = pid
        self.name = name
        self.des = des
        self.price = price
        self.producer = producer
        self.img = img
        self.tags = tags


def save(pl):
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='pretty_cat', charset='UTF8')
    cur = conn.cursor()
    if not cur.execute("show tables like 'product'"):
        createSql = """CREATE TABLE PRODUCT (
            ID NVARCHAR(20) PRIMARY KEY,
            NAME NVARCHAR(100),
            PRICE DOUBLE,
            IMG NVARCHAR(200),
            DES NVARCHAR(500),
            PRODUCER NVARCHAR(100),
            TAGS NVARCHAR(100)
         )"""
        print(createSql)
        cur.execute(createSql)
        for product in pl:
            sql = "INSERT INTO PRODUCT(ID, NAME, PRICE, IMG, DES, PRODUCER, TAGS) VALUES ('%s','%s','%d','%s','%s','%s','%s')" \
                  % (product.id, product.name, float(product.price), product.img, product.des, product.producer, ",".join(product.tags))
            print(sql)
            cur.execute(sql)
            conn.commit()
        return
    for product in pl:
        searchSql = "SELECT * FROM PRODUCT WHERE ID = '%s'" % product.id
        if not cur.execute(searchSql):
            sql = "INSERT INTO PRODUCT(ID, NAME, PRICE, IMG, DES, PRODUCER, TAGS) VALUES ('%s','%s','%d','%s','%s','%s','%s')" \
                  % (product.id, product.name, float(product.price), product.img, product.des, product.producer, ",".join(product.tags))
        else:
            sql = "UPDATE PRODUCT SET NAME = '%s', PRICE = '%d', IMG = '%s', DES = '%s', PRODUCER = '%s', TAGS = '%s' WHERE ID = '%s'" \
                  % (product.name, float(product.price), product.img, product.des, product.producer, ",".join(product.tags), product.id)
        print(sql)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()


def o2j(p):
    return {
        "id": p.id,
        "name": p.name,
        "price": p.price,
        "img": p.img,
        "des": p.des,
        "producer": p.producer,
        "tags": p.tags
    }


if __name__ == '__main__':
    zr = zhangui()
    productList = zr.downLoad()
    save(productList)
    print("=============完成=============")
