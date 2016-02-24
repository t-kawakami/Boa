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
    tr_list = main_table.tbody.find_all('tr')
    date_time_list = [tr.find_all('td')[0].text for tr in tr_list]
    start_value_list = [tr.find_all('td')[1].text for tr in tr_list]
    high_value_list = [tr.find_all('td')[2].text for tr in tr_list]
    low_value_list = [tr.find_all('td')[3].text for tr in tr_list]
    end_value_list = [tr.find_all('td')[4].text for tr in tr_list]
    amount_list = [tr.find_all('td')[5].text for tr in tr_list]
    total_value_list = [tr.find_all('td')[6].text for tr in tr_list]

    for value in date_time_list:
        print(value)

    valid_value = delete_invalid(date_time_list, end_value_list)
    print(calc_move_average(valid_value, 5))
    print(calc_move_average(valid_value, 10))
    print(calc_move_average(valid_value, 15))

# 無効な値を除外し、有効な値の時刻と一緒に返す
def delete_invalid(date_time_list, value_list):
    valid_value = [(date_time, value) for date_time, value in zip(date_time_list, value_list) if value != '-']
    return valid_value

# windowサイズ幅で移動平均を計算する
def calc_move_average(datas, window):
    datas = np.asarray(datas, dtype='float32')
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
            os.mkdir('../data/%s' % date)
        write_file = open('../data/%s/%s_%s.txt' % (date, code, name), 'w')
        soup = BeautifulSoup(html, 'lxml')
        main_table = soup.find(id='maintable')
        write_file.write(str(main_table))
        write_file.close()
        return main_table
    else:
        main_table = BeautifulSoup(open('../data/%s/%s_%s.txt' % (date, code, name), 'r'), 'lxml')
        return main_table

def main(from_row=2, to_row=100):
    all_data = pandas.read_csv('../data/all_2016-02-22.csv', encoding='utf-8')
    code_list = all_data[u'コード']
    name_list = all_data[u'銘柄名']
    for index in xrange(0, len(code_list)):
        # ヘッダ行と該当行を除くため2引く
        if index < (from_row - 2) | index >= (to_row - 2):
            continue
        code = code_list[index]
        name = name_list[index]
        print('%s_%s_%s' % (index + 2, code, name))
        get_stock(code, name, '2016-02-23', download=False)

if __name__ == '__main__':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
    main(from_row=436, to_row=436)
