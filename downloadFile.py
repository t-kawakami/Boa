__author__ = 'kawakami_note'
import urllib.request

def download(url, title):
    urllib.request.urlretrieve(url, title)

file = open("data/input.txt", "r", encoding="UTF-8")
for line in file:
    line.split()
    download(line.split()[0], "data/" + line.split()[1])