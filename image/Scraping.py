# -*- coding: utf-8 -*-
__author__ = 'kawakami_note'

import pandas as pd
import urllib2
from bs4 import BeautifulSoup

# img srcを抽出する
def extract_img_src():
    csv = pd.read_csv('data/scraping.csv')
    urls, tags = csv['url'], csv['tag']
    img_tag, img_url = [], []
    for url, tag in zip(urls, tags):
        soup = BeautifulSoup(urllib2.urlopen(url), 'lxml')
        img_all = soup.find_all('img')
        for img in img_all:
            img_tag.append(tag)
            img_url.append(img)
    pd.DataFrame({"tag":img_tag, "url":img_url}).to_csv("data/tag_url.csv")

if __name__ == '__main__':
    extract_img_src()
