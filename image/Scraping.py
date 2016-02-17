# -*- coding: utf-8 -*-
__author__ = 'kawakami_note'

import pandas as pd
import urllib2
from bs4 import BeautifulSoup

# サイトのHTMLを取得し、ファイルに出力する。(JavaScriptで展開するHTMLが含まれるため)
def get_html():
    csv = pd.read_csv('data/scraping.csv')
    file_names, urls= csv['file'], csv['url']
    for file_name, url in zip(file_names, urls):
        write_file = open(file_name, 'w')
        write_file.write(urllib2.urlopen(url).read())


# img srcを抽出する
def extract_img_src():
    csv = pd.read_csv('data/scraping.csv')
    file_names, tags = csv['file'], csv['tag']
    for file_name, tag in zip(file_names, tags):
        html_file = open(file_name, 'r')
        html = ''.join(html_file.readlines())
        soup = BeautifulSoup(html, 'html.parser')
        img_all = soup.find_all('img')
        for img in img_all:
            print(img)

def main(read_html=True):
    if read_html:
        get_html()
    extract_img_src()

if __name__ == '__main__':
    main(read_html=True)
