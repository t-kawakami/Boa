# -*- coding: utf-8 -*-
__author__ = 'kawakami_note'
import urllib
import csv

def download(url, title):
    urllib.urlretrieve(url, title)

def main(from_index):
    input_file = open("data/input.csv", "r")
    mapping_file = open("data/mapping.csv", "w")
    lines = csv.reader(input_file, delimiter=",")

    index = 0
    for line in lines:
        index += 1
        if index <= from_index:
            continue
        file_name = "data/images/" + str(index).zfill(10) + ".jpg"
        print('processing:' + file_name)
        # download(line[0], file_name)
        # TODO 余計に改行が入ってしまう。
        writer = csv.writer(mapping_file, delimiter=',',quotechar='|')
        writer.writerow([file_name, line[1]])

if __name__ == "__main__":
    main(0)