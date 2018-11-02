# -*- coding:UTF-8 -*-
import requests
import json
from lxml import etree


if __name__ == '__main__':
    target = 'https://nj.fang.anjuke.com/loupan/s?kw='
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }
    req = requests.get(url=target, headers=headers)
    html = etree.HTML(req.text)
    div_list = html.xpath("//div[@class='item-mod ']")
    item_list = []
    for div in div_list:
        item = {"name": div.xpath(".//h3/span[@class='items-name']/text()"),
                "price": div.xpath(".//p[@class='price']//text()")}
        item_list.append(item)
    
    with open("wj.txt", "a" ,encoding="utf-8") as f:
        for item in item_list:
            f.write(json.dumps(item, ensure_ascii=False))
            f.write("\n")
        print("保存成功")
