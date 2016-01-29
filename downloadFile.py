__author__ = 'kawakami_note'
import urllib
import csv

def download(url, title):
    urllib.urlretrieve(url, title)

file = open("data/input.csv", "r")
lines = csv.reader(file, delimiter=",")

for line in lines:
    download(line[0], "data/" + line[1])
