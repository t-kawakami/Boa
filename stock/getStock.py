# -*- coding: utf-8 -*-
__author__ = 'kawakami_note'

import urllib
import pandas
from bs4 import BeautifulSoup

def download_csv():
    all_data = pandas.read_csv('data/all_2016-02-22.csv')
    code = all_data['コード']
    url = 'http://k-db.com/stocks/8306-T/5min'
    html = urllib.urlopen(url)
    soup = BeautifulSoup(html, 'lxml')
    soup.find_all()
    print(soup)

def main():
    download_csv()

if __name__ == '__main__':
    main()