from selenium import webdriver
from lxml import etree
import json

browser = webdriver.Chrome()

browser.get("http://www.biqukan.com/1_1094/5403177.html")
h = browser.page_source
browser.close()
print(h)
html = etree.HTML(h)
text = html.xpath("//div[@class='showtxt']//text()")
print(text)
with open("xs.txt", "a", encoding="utf-8") as f:
    for t in text:
        f.write(t.strip())
        f.write("\n")
    print("保存成功")
