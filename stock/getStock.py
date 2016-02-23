# -*- coding: utf-8 -*-
__author__ = 'kawakami_note'

import urllib
import pandas
from bs4 import BeautifulSoup
import os
import sys
import codecs
import numpy as np

def get_stock(code, name, date, download=False):
    main_table = get_main_table(code, name, date, download)
    # 日時、始値、高値、安値、終値、出来高、売買代金を取得する
    # tr_list = main_table.tbody.find_all('tr')
    # date_time_list = [tr.find_all('td')[0].text for tr in tr_list]
    # start_value_list = [tr.find_all('td')[1].text for tr in tr_list]
    # high_value_list = [tr.find_all('td')[2].text for tr in tr_list]
    # low_value_list = [tr.find_all('td')[3].text for tr in tr_list]
    # end_value_list = [tr.find_all('td')[4].text for tr in tr_list]
    # amount_list = [tr.find_all('td')[5].text for tr in tr_list]
    # total_value_list = [tr.find_all('td')[6].text for tr in tr_list]

# windowサイズ幅で移動平均を計算する
def calc_move_average(datas, window):
    datas = np.asarray(datas)
    tmp = np.ones(window) / window
    return np.convolve(datas, tmp, 'valid')

# データを読み込む
def get_main_table(code, name, date, download=False):
    # 禁則文字を置換する
    code = code.replace('/', '')
    name = name.replace('/', '')
    if download:
        url = 'http://k-db.com/stocks/%s-T/5min' % code
        html = urllib.urlopen(url).read()
        if not os.path.exists('data/%s' % date):
            os.mkdir('data/%s' % date)
        write_file = open('data/%s/%s_%s.txt' % (date, code, name), 'w')
        soup = BeautifulSoup(html, 'lxml')
        main_table = soup.find(id='maintable')
        print(name)
        write_file.write(str(main_table))
        write_file.close()
        return main_table
    else:
        main_table = BeautifulSoup(open('data/%s/%s_%s.txt' % (date, code, name), 'r'), 'lxml')
        print(name)
        return main_table

def main(skip_num=0):
    all_data = pandas.read_csv('data/all_2016-02-22.csv', encoding='utf-8')
    code_list = all_data[u'コード']
    name_list = all_data[u'銘柄名']
    index = 0
    for index in xrange(0, len(code_list)):
        if index < skip_num:
            continue
        get_stock(code_list[index], name_list[index], '2016-02-23', download=True)

if __name__ == '__main__':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
    main(skip_num=166)