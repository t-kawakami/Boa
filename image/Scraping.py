# -*- coding: utf-8 -*-
__author__ = 'kawakami_note'

import pandas as pd
import urllib2
from bs4 import BeautifulSoup

def extract_img_src():
    csv = pd.read_csv('data/scraping.csv')
    file_names, urls= csv['file'], csv['url']
    for file_name, url in zip(file_names, urls):
        html = urllib2.urlopen(url).read()
        soup = BeautifulSoup(html, 'lxml')
        img_all = soup.find_all('img')
        for img in img_all:
            print(img['src'])

def main():
    extract_img_src()

if __name__ == '__main__':
    main()
