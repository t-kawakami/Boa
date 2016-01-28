__author__ = 'kawakami_note'
import urllib.request
import csv

def download(url, title):
    urllib.request.urlretrieve(url, title)

file = open("data/input.csv", "r", encoding="UTF-8")
lines = csv.reader(file, delimiter=",")

for line in lines:
    download(line[0], "data/" + line[1])
