# -*- coding: utf-8 -*-
__author__ = 'kawakami_note'

import urllib
import pandas
from bs4 import BeautifulSoup
import os

def get_stock(code, date, download=False):
    main_table = get_main_table(code, date, download)
    # 日時、始値、高値、安値、終値、出来高、売買代金を取得する
    # tr_list = main_table.tbody.find_all('tr')
    # date_time_list = [tr.find_all('td')[0].text for tr in tr_list]
    # start_value_list = [tr.find_all('td')[1].text for tr in tr_list]
    # high_value_list = [tr.find_all('td')[2].text for tr in tr_list]
    # low_value_list = [tr.find_all('td')[3].text for tr in tr_list]
    # end_value_list = [tr.find_all('td')[4].text for tr in tr_list]
    # amount_list = [tr.find_all('td')[5].text for tr in tr_list]
    # total_value_list = [tr.find_all('td')[6].text for tr in tr_list]

# データを読み込む
def get_main_table(code, date, download=False):
    if download:
        url = 'http://k-db.com/stocks/%s-T/5min' % code
        html = urllib.urlopen(url).read()
        if not os.path.exists('data/%s' % date):
            os.mkdir('data/%s' % date)
        write_file = open('data/%s/%s.txt' % (date, code), 'w')
        soup = BeautifulSoup(html, 'lxml')
        main_table = soup.find(id='maintable')
        print(main_table)
        write_file.write(str(main_table))
        write_file.close()
        return main_table
    else:
        main_table = BeautifulSoup(open('data/%s/%s.txt' % date, code, 'r'), 'lxml')
        return main_table

def main():
    all_data = pandas.read_csv('data/all_2016-02-22.csv')
    code_list = all_data['コード']
    for code in code_list:
        get_stock(code, '2016-02-22', download=True)

if __name__ == '__main__':
    main()