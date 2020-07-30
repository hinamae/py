# BeautifulSoup
# HTMLやXMLを取得するモジュール
# Webスクレイピングでは、かなり広く使われている
# pip install beautifulsoup4

・HTMLパーサーの選択
・タグによる検索
・属性による条件検索
・正規表現による検索
・HTML整形出力
※Xpathによる検索はできない

import requests
import pprint
import re

from bs4 import BeautifulSoup

def main():

    url  = "https://www.yahoo.co.jp/"
    res  = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    pprint.pprint(soup, width=40)

    a    = soup.find_all("a")
    pprint.pprint(soup, width=40)

    tr    = soup.find_all("tr")
    pprint.pprint(tr[40], width=40)

    img     = soup.find_all("img")
    pprint.pprint(img[0], width=40)
    print(img[0].get("src"))

    # 条件指定した検索
    for i in soup.find_all("td", valign="top"):
        print(i)
        print("-------------------------------------")

    # 正規表現で条件指定した検索
    for i in soup.find_all("a", href=re.compile("http.*yahoo")):
        print(i)
        print("-------------------------------------")

    # CSSセレクタを使った検索
    print(soup.select("#p"))

    # 整形出力
    print(soup.prettify())
